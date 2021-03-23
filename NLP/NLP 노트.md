
## 형태소 분석기 - KoNLPy
- Kkma, Komoran, Okt, Hannanum, Mecab
<br>

#### 기본 사용법

`pos(문장)` : 형태소와 품사를 태깅하여 반환 (POS tagger)<br>
`morphs(문장)` : 형태소만 반환<br>
`nouns(문장)` : 명사인 형태소만 반환<br>

<br>

```
# Kkma 분석기 이용
from konlpy.tag import Kkma
kkma = Kkma()

sentence = "치킨은 맛있다. 콜라는 최고다."
print(kkma.morphs(sentence))  # ['치킨', '은', '맛있', '다', '.', '콜라', '는', '최고', '이', '다', '.']
print(kkma.nouns(sentence)) # ['치킨', '콜라', '최고']
print(kkma.pos(sentence)) # [('치킨', 'NNG'), ('은', 'JX'), ('맛있', 'VA'), ('다', 'EFN'), ('.', 'SF'), ('콜라', 'NNG'), ('는', 'JX'), ('최고', 'NNG'), ('이', 'VCP'), ('다', 'EFN'), ('.', 'SF')]
```

<br><br>

#### 사용자 사전 구축
- 형태소 분석이 제대로 되지 않는 단어를 사용자가 추가할 수 있다.
- Komoran을 이용하는 것이 가장 간단하다.

방법
1. 현재 경로에 'user_dic.txt' 파일을 만든다. (파일명, 확장자 상관 X)
2. 등록할 단어 - Tab 키 - 품사(생략 시 NNG) 순으로 파일에 입력한다.
3. Komoran 객체 생성 시 userdic 인자에 파일명을 넣어준다. ex) `komoran = Komoran(userdic='./user_dic.txt')`

<br><br><br><hr><br>



## 임베딩
- 단어나 문장을 벡터로 표현하는 과정
- 자연어를 컴퓨터가 이해할 수 없기 때문에 연산 가능한 형태로 변환한다
<br>

### 문장 임베딩
- 문장 전체를 벡터로 표현
- 장점 : 문장의 흐름을 파악해 벡터로 변환하여 문맥적 의미를 지님
- 단점 : 많은 데이터 필요, 높은 비용
<br>


### 단어 임베딩  -> good !
- 개별 단어를 벡터로 표현
- 장점 : 방법이 간단하여 많이 사용
- 단점 : 동음이의어도 동일한 벡터 값으로 표현됨

#### 희소 표현 (= one-hot 인코딩)
1. 문장으로부터 단어 사전 구축   _(ex: ['오늘', '날씨', '구름'])_
2. 단어 사전의 각 단어에 순서대로 인덱스 부여   _(ex: [0, 1, 2])_
3. 인덱스 번호에 해당하는 위치에 one-hot 인코딩   _(ex: [1, 0, 0], [0, 1, 0], [0, 0, 1])_

- 장점 : 간단함
- 단점 : 단어의 수가 많아지면 계산량과 공간 측면에서 비효율적임, 단어 간의 연관성이 없음


#### 분산 표현(밀집 표현) -> good !
- 한 단어의 정보가 특정 차원에만 표현되지 않고, 여러 차원에 분산되어 표현된다
- 장점1 : 데이터 손실을 최소화하면서 임베딩 벡터의 차원을 압축
- 장점2 : 단어의 의미, 단어 간 연관성에 대한 정보를 가짐
- 유사한 의미를 갖는 단어들은 벡터 공간 상에서 가까이 위치

##### Word2Vec
- 대표적인 신경망 기반 단어 임베딩 모델
- 분산 표현 형태
- CBOW
  - 주변 단어(맥락)를 이용해 타겟 단어를 예측
  - 학습 속도 빠름
- skip-gram
  - 타겟 단어를 이용해 주변 단어를 예측
  - 계산량 많음, 임베딩 품질이 높음

`from gensim.models import Word2Vec`<br>

- Word2Vec 모델 생성 : `model = Word2Vec(sentences, size, window, hs, min_count, sg)`
  - sentences : 학습할 단어 리스트
  - size : 단어 임베딩 벡터의 차원(크기)
  - window : 주변 단어 윈도우의 크기
  - hs : 0(0이 아니면 음수 샘플링 사용), 1(모델 학습에 softmax 사용)
  - min_count : 단어 최소 빈도 수 (이 빈도 수 이하의 단어는 학습 X)
  - sg : 0(CBOW), 1(skip-gram)

- 모델 저장 : `model.save('모델명.model')`<br>
- 모델 불러오기 : `model = Word2Vec.load('모델명.model')`<br>
- 워드 임베딩 벡터 생성 : `model.wv['단어']`<br>
- 두 단어 간 유사도 계산 : `model.wv.similarity(w1='단어1', w2='단어2')`<br>
- 가장 유사한 단어 추출 : `model.wv.most_similar('단어', topn) # topn은 추출할 단어 수`<br>

<br><br><br><hr><br>



## 텍스트 

#### n-gram 유사도

1. 문장에서 단어만 추출
2. slicing 이용하여 n-gram으로 토큰 분리
3. 유사도 계산 식 = 문장1과 문장2에서 동일한 토큰 수 / 문장1의 전체 토큰 수

- n이 너무 크면 동일한 토큰을 파악할 때 정확도가 떨어짐
- n이 너무 작으면 문맥을 파악하는 정확도가 떨어짐
- n은 1~5 값으로 많이 사용

<br>

#### 코사인 유사도

- 단어나 문장을 벡터로 표현하고, 두 벡터 간 코사인 각도를 구해 유사도를 측정
- 유사도 계산 식 = 두 벡터의 내적(_dot_) / 각 벡터의 크기(_norm_) 곱
- n-gram 유사도보다 정확

<br><br><br><hr><br>



## 딥러닝 모델

- 역전파 시 편미분을 통해 오차를 줄일 수 있는 weight의 변화 방향의 크기를 계산함
- Sigmoid 함수는 학습 시 층이 깊어질수록 미분 값이 0으로 수렴하기 때문에, 역전파 시 weight가 갱신되지 않아 학습이 되지 않을 수 있음
- 이에 따라 hidden layer에서는 ReLU 함수를, Output layer에서 Sigmoid 함수를 주로 사용한다

<br><br><br><hr><br>



## LSTM (Long Short Term Memory)

- RNN의 문제점 : 입력 시퀀스가 길거나 RNN을 다층 구조로 쌓으면, 앞쪽의 데이터가 뒤쪽으로 잘 전달되지 않음
- 이러한 RNN의 문제점을 보완하기 위한 모델
- hidden state 계산 방식 변경, cell state 추가
- Input Gate
  - 현재 데이터를 얼마나 기억할지를 결정

  ![image](https://user-images.githubusercontent.com/37769713/109601999-310f5800-7b63-11eb-8837-bcd1b15ab92a.png)

- Forget Gate
  - 이전 cell state를 얼마나 기억할지를 결정

  ![image](https://user-images.githubusercontent.com/37769713/109602437-6ddb4f00-7b63-11eb-8bb2-fdad222fdb76.png)

- Output Gate
  - 현재 hidden state를 결정하는데에 영향을 줌

  ![image](https://user-images.githubusercontent.com/37769713/109602577-b7c43500-7b63-11eb-9581-d942d7ec5251.png)

- 현재 cell state

  ![image](https://user-images.githubusercontent.com/37769713/109602800-26a18e00-7b64-11eb-8eff-ede551bc504f.png)

- 현재 hidden state

  ![image](https://user-images.githubusercontent.com/37769713/109602635-d4f90380-7b63-11eb-8929-23fc9fcbbfc2.png)

<br>

### 양방향(Bidriectional) LSTM 

- RNN은 데이터를 입력 순서로 처리하기 때문에 바로 이전 시점의 정보만 활용할 수 있음
- 문장이 길어질 수록 성능이 저하
- 따라서, 기존 LSTM에 역방향으로 처리하는 LSTM 계층을 추가하여 양방향에서 처리할 수 있도록 함
- `Bidirectional(LSTM())`에서 return_sequences 인자를 반드시 True로 해야 함


<br><br><br><hr><br>

## 단어의 의미를 파악하는 방법
1. 시소러스(유의어 사전) 활용 기법
  - 사람이 수작업으로 처리하기 때문에 한계가 많음
  - 대표적으로 WordNet
2. 통계 기반 기법
  - 

3. 추론 기반 기법 - word2vec
