import pandas as pd
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate


#################### 감성 분석 모델 생성 및 저장 ####################

# 데이터 읽어오기
train_file = './chatbot_data.csv'
data = pd.read_csv(train_file, delimiter=',', encoding='CP949')
features = data['Q'].tolist()
labels = data['label'].tolist()

# 단어 인덱스 시퀀스 벡터
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus)    # 시퀀스 번호로 변환
word_index = tokenizer.word_index

MAX_SEQ_LEN = 15    # 시퀀스 벡터 크기
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')   # 패딩

ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))
ds = ds.shuffle(len(features))  # 데이터 섞기

# 학습:검증:테스트 데이터 비율 = 7:2:1
train_size = int(len(padded_seqs)*0.7)
val_size = int(len(padded_seqs)*0.2)
test_size = int(len(padded_seqs)*0.1)
train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size+val_size).take(test_size).batch(20)

# 하이퍼파라미터 설정
dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(word_index) + 1  # 전체 단어 수

# CNN 모델 정의
input_layer = Input(shape=(MAX_SEQ_LEN, ))  # 시퀀스 벡터를 입력으로 받음
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length=MAX_SEQ_LEN)(input_layer)    # 희소 벡터인 시퀀스 벡터를 받아 밀집 벡터로 변환
dropout_emb = Dropout(rate=dropout_prob)(embedding_layer)   # overfitting 방지

conv1 = Conv1D(
    filters=128,
    kernel_size=3,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool1 = GlobalMaxPool1D()(conv1)

conv2 = Conv1D(
    filters=128,
    kernel_size=4,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool2 = GlobalMaxPool1D()(conv2)

conv3 = Conv1D(
    filters=128,
    kernel_size=5,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool3 = GlobalMaxPool1D()(conv3)

concat = concatenate([pool1, pool2, pool3]) # feature map을 하나로 합침


hidden = Dense(128, activation=tf.nn.relu)(concat)  # fully-connected layer, 출력 노드 128개
dropout_hidden = Dropout(rate=dropout_prob)(hidden)
logits = Dense(3, name='logits')(dropout_hidden)    # 출력 노드 3개, 최종 예측이므로 활성화 함수 사용X, 가장 높은 점수를 갖는 노드가 예측의 결과

predictions = Dense(3, activation=tf.nn.softmax)(logits)    # 학습 단계에서 cross-entropy 계산을 위해 확률 값이 필요하므로 softmax 사용


model = Model(inputs=input_layer, outputs=predictions)  # 앞에서 정의한 계층들을 추가하여 케라스 모델 생성
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])         # 모델 컴파일
model.fit(train_ds, validation_data=val_ds, epochs=EPOCH, verbose=1)    # 모델 학습

loss, accuracy = model.evaluate(test_ds, verbose=1) # 성능 평가
print('Accuracy: %f' % (accuracy*100))  # 98.646361
print('loss: %f' % (loss))  # 0.043508

model.save('cnn_model.h5')  # 모델 저장





#################### 모델 로드해서 감성 분석 해보기 #######################

# 데이터 읽어오기
train_file = './chatbot_data.csv'
data = pd.read_csv(train_file, delimiter=',', encoding='CP949')
features = data['Q'].tolist()
labels = data['label'].tolist()

# 단어 인덱스 시퀀스 벡터
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus)

MAX_SEQ_LEN = 15    # 시퀀스 벡터 크기
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

# 테스트용 데이터셋 생성
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))
ds = ds.shuffle(len(features))
test_ds = ds.take(2000).batch(20)

# 감성 분석 CNN 모델 불러오기
model = load_model('cnn_model.h5')
model.summary()
model.evaluate(test_ds, verbose=2)

# 테스트용 데이터셋의 10212번째 데이터 출력
print("단어 시퀀스 : ", corpus[10212])   # ['썸', '타는', '여자가', '남사친', '만나러', '간다는데', '뭐라', '해']
print("단어 인덱스 시퀀스 : ", padded_seqs[10212])  # [   13    61   127  4320  1333 12162   856    31     0     0     0     0     0     0     0]
print("문장 분류(정답) : ", labels[10212])    # 2

# 테스트용 데이터셋의 10212번째 데이터의 감성 분석
picks = [10212]
predict = model.predict(padded_seqs[picks])     # 입력 데이터에 대해 각 클래스의 예측 점수를 반환
predict_class = tf.math.argmax(predict, axis=1) # 예측 점수가 가장 큰 클래스 번호 반환
print("감정 예측 점수 : ", predict)   # [[3.4995098e-06 2.6420976e-06 9.9999380e-01]]
print("감정 예측 클래스 : ", predict_class.numpy())    # [2]
