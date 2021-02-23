
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

<br><br><br>

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
- 워드 임베딩 벡터 생성 : `model.wv[단어]`<br>
- 두 단어 간 유사도 계산 : `model.wv.similarity(w1='단어1', w2='단어2')`<br>
- 가장 유사한 단어 추출 : `model.wv.most_similar('단어', topn) # topn은 추출할 단어 수`<br>

<br><br>


