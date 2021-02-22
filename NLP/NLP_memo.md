
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

