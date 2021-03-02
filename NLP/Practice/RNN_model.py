import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, LSTM, SimpleRNN


# time step만큼 시퀀스 데이터 분리
def split_sequence(sequence, step):
    x, y = list(), list()

    for i in range(len(sequence)):
        end_idx = i+step
        if end_idx > len(sequence)-1:
            break

        seq_x, seq_y = sequence[i:end_idx], sequence[end_idx]
        x.append(seq_x)
        y.append(seq_y)

    return np.array(x), np.array(y)

# 하이퍼파라미터
n_timesteps = 15    # 입력 시퀀스 길이
n_features = 1  # 입력 벡터의 dimension 크기

# sin 함수 학습 데이터
x = [i for i in np.arange(start=-10, stop=10, step=0.1)]
train_y = [np.sin(i) for i in x]
train_x, train_y = split_sequence(train_y, step=n_timesteps)    # 시퀀스 나누기
print("shape x:{} / y:{}".format(train_x.shape, train_y.shape))

# RNN 입력 벡터 크기를 맞추기 위해 벡터 dimenstion 크기 변경 (Keras에서 RNN 계층을 사용하려면 3차원 텐서여야 하기 때문)
train_x = train_x.reshape(train_x.shape[0], train_x.shape[1], n_features)   # [samples, timesteps] -> [samples, timesteps, features]
print("train_x.shape = {}".format(train_x.shape))
print("train_y.shape = {}".format(train_y.shape))

# RNN 모델 정의
model = Sequential()
# SimpleRNN 대신 LSTM을 쓰면 LSTM 모델이 됨
model.add(SimpleRNN(units=10,
                    return_sequences=False,
                    input_shape=(n_timesteps, n_features))) # units: RNN 계층에 존재하는 노드 수, return_sequences: hidden state를 모든 과정에서 출력할 것인지
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# RNN 모델 학습
np.random.seed(0)
from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(
    monitor='loss',
    patience=5,
    mode='auto')    # overfitting 방지를 위해 loss가 갑자기 증가하는 시점을 찾을 수 있는 EarlyStopping 콜백 객체 사용
history = model.fit(train_x, train_y, epochs=1000, callbacks=[early_stopping])

# loss 그래프 출력
plt.plot(history.history['loss'], label='loss')
plt.legend(loc="upper right")
plt.show()

# 테스트 데이터셋 생성
test_x = np.arange(10, 20, step=0.1)
calc_y = np.cos(test_x)     # sin 함수를 이용하면 학습 데이터와 같기 때문에 cos 함수를 이용해 테스트

# RNN 모델 예측 및 로그 저장
test_y = calc_y[:n_timesteps]
for i in range(len(test_x)-n_timesteps):
    net_input = test_y[i:i+n_timesteps]
    net_input = net_input.reshape((1, n_timesteps, n_features))
    predict_y = model.predict(net_input)
    test_y = np.append(test_y, predict_y)

# 예측 결과 그래프 출력
plt.plot(test_x, calc_y, label="ground truth", color="orange")
plt.plot(test_x, test_y, label="predictions", color="blue")
plt.legend(loc="upper left")
plt.ylim(-2, 2)
plt.show()

