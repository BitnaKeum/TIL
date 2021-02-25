from konlpy.tag import Komoran
import numpy as np
from numpy import dot
from numpy.linalg import norm


################### n-gram 유사도 계산 #########################

# 어절 단위 n-gram 계산
def word_ngram(bow, num_gram):
    text = tuple(bow)
    ngrams = [text[x:x+num_gram] for x in range(len(text))]
    return tuple(ngrams)

# 유사도 계산
def similarity(doc1, doc2):
    cnt = 0
    for token in doc1:
        if token in doc2:
            cnt += 1
    return cnt/len(doc1)

sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학했다.'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학했다.'
sentence3 = '나는 맛있는 밥을 뉴턴 선생님과 함께 먹었다.'

komoran = Komoran()

# 명사 형태소 추출
bow1 = komoran.nouns(sentence1)
bow2 = komoran.nouns(sentence2)
bow3 = komoran.nouns(sentence3)

# 2-gram 토큰 추출
doc1 = word_ngram(bow1, 2)
doc2 = word_ngram(bow2, 2)
doc3 = word_ngram(bow3, 2)

# 유사도 계산
r1 = similarity(doc1, doc2)
r2 = similarity(doc3, doc1)

print(r1) # 0.6666
print(r2) # 0

#################################################################



################### 코사인 유사도 계산 #########################

# 코사인 유사도 계산
def cos_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1)*norm(vec2))

# 단어 문서 행렬(TDM) 생성
def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}

    for word in word_dics:
        freq_mat[word] = 0

    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1

    return freq_mat

# 단어 벡터 생성
def make_vector(tdm):
    vec = []
    for key in tdm:
        vec.append(tdm[key])
    return vec

sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학했다.'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학했다.'
sentence3 = '나는 맛있는 밥을 뉴턴 선생님과 함께 먹었다.'

komoran = Komoran()

# 명사 형태소 추출
bow1 = komoran.nouns(sentence1)
bow2 = komoran.nouns(sentence2)
bow3 = komoran.nouns(sentence3)

# 단어 리스트 합침
bow = bow1 + bow2 + bow3

# 단어 리스트에서 중복을 제거해 단어 사전 구축
word_dics = []
for token in bow:
    if token not in word_dics:
        word_dics.append(token)

# 문장마다 단어 문서 행렬 생성
freq_list1 = make_term_doc_mat(bow1, word_dics)
freq_list2 = make_term_doc_mat(bow2, word_dics)
freq_list3 = make_term_doc_mat(bow3, word_dics)

# 문장 벡터 생성
doc1 = np.array(make_vector(freq_list1))
doc2 = np.array(make_vector(freq_list2))
doc3 = np.array(make_vector(freq_list3))

# 코사인 유사도 계산
r1 = cos_similarity(doc1, doc2)
r2 = cos_similarity(doc3, doc1)

print(r1) # 0.8333333333333335
print(r2) # 0.20412414523193154

#################################################################
