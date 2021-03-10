import tensorflow as tf
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
from utils.Preprocess import Preprocess

# 학습 파일 불러오기
def read_file(file_name):
    sents = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if l[0] == ';' and lines[idx+1][0] == '$':
                this_sent = []
            elif l[0] == '$' and lines[idx-1][0] == ';':
                continue
            elif l[0] == '\n':
                sents.append(this_sent)
            else:
                this_sent.append(tuple(l.split()))
    return sents

# 전처리 객체 생성
p = Preprocess(word2index_dic='../../train_tools/dict/chatbot_dict.bin', userdic='../../utils/user_dic.tsv')

# 학습용 말뭉치 데이터를 불러옴
corpus = read_file('ner_train.txt')

# 말뭉치 데이터에서 단어와 BIO 태그만 불러와 학습용 데이터셋 생성
sentences, tags = [], []
for t in corpus:
    tagged_sentence = []
    sentence, bio_tag = [], []
    for w in t:
        tagged_sentence.append((w[1], w[3]))
        sentence.append(w[1])
        bio_tag.append(w[3])

    sentences.append(sentence)
    tags.append(bio_tag)

print("샘플 크기 : ", len(sentences))
print("0번째 샘플 단어 시퀀스 : ", sentences[0])
print("0번째 샘플 bio 태그 : ", tags[0])
print("샘플 단어 시퀀스 최대 길이 : ", max(len(l) for l in sentences))
print("샘플 단어 시퀀스 평균 길이 : ", (sum(map(len, sentences))/len(sentences)))

# 토크나이저 정의
tag_tokenizer = preprocessing.text.Tokenizer(lower=False)
tag_tokenizer.fit_on_texts(tags)

# 단어 사전 및 태그 사전 크기
vocab_size = len(p.word_index) + 1
tag_size = len(tag_tokenizer.word_index) + 1
print("단어 사전 크기 : ", vocab_size)
print("BIO 태그 사전 크기 : ", tag_size)

# 학습용 단어 시퀀스 생성
x_train = [p.get_wordidx_sequence(sent) for sent in sentences]
y_train = tag_tokenizer.texts_to_sequences(tags)

index_to_ner = tag_tokenizer.index_word # 시퀀스 인덱스를 NER로 변환하기 위해 사용
index_to_ner[0] = 'PAD'

# 시퀀스 패딩 처리
max_len = 40
x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=max_len, padding='post')
y_train = preprocessing.sequence.pad_sequences(y_train, maxlen=max_len, padding='post')

# 학습 데이터 : 테스트 데이터 = 8 : 2
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=.2, random_state=1234)

# 출력 데이터를 원핫 인코딩
y_train = tf.keras.utils.to_categorical(y_train, num_classes=tag_size)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=tag_size)

print("학습 샘플 시퀀스 shape : ", x_train.shape)
print("학습 샘플 레이블 shape : ", y_train.shape)
print("테스트 샘플 시퀀스 shape : ", x_test.shape)
print("테스트 샘플 레이블 shape : ", y_test.shape)

# 모델 정의 (Bi-LSTM)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from tensorflow.keras.optimizers import Adam

model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=30, input_length=max_len, mask_zero=True))
model.add(Bidirectional(LSTM(200, return_sequences=True, dropout=0.50, recureent_dropout=0.25)))
model.add(TimeDistributed(Dense(tag_size, activation='softmax')))
model.compile(loss='categorical_crossentropy', optimizer=Adam(0.01), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=128, epochs=10)

print("평가 결과 : ", model.evaluate(x_test, y_test)[1])
model.save('ner_model.h5')

# 시퀀스를 NER 태그로 변환
def sequences_to_tag(sequences):    # 예측값을 index_to_ner를 사용하여 태깅 정보로 변경하는 함수
    result = []
    for sequence in sequences:
        temp = []
        for pred in sequence:
            pred_
### p.257