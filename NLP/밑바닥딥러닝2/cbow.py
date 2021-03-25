import sys
sys.path.append('..')
import numpy as np
from common.layers import MatMul, SoftmaxWithLoss

class SimpleCBOW:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size

        # 가중치 초기화
        W_in = 0.01 * np.random.randn(V, H).astype('f') # 부동소수점
        W_out = 0.01 * np.random.randn(H, V).astype('f')

        # 계층 생성
        self.input_layer0 = MatMul(W_in)
        self.input_layer1 = MatMul(W_in)
        self.output_layer = MatMul(W_out)
        self.loss_layer = SoftmaxWithLoss()

        # 모든 가중치와 기울기를 리스트에 모음
        layers = [self.input_layer0, self.input_layer1, self.output_layer]
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads   # forward() 호출 후 backward()를 호출하면 grads에 저장된 기울기가 갱신됨

        # 인스턴스 변수에 단어의 분산 표현을 저장
        self.word_vecs = W_in

    def forward(self, contexts, target):
        hidden_layer0 = self.input_layer0.forward(contexts[:, 0])
        hidden_layer1 = self.input_layer1.forward(contexts[:, 1])
        hidden_layer = (hidden_layer0 + hidden_layer1) * 0.5
        score = self.output_layer.forward(hidden_layer)
        loss = self.loss_layer.forward(score, target)
        return loss

    def backward(self, dout=1):
        ds = self.loss_layer.backward(dout)
        da = self.output_layer.backward(ds)
        da *= 0.5
        self.input_layer1.backward(da)
        self.input_layer0.backward(da)
        return None
