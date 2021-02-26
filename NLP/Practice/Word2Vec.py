from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

# 네이버 영화 리뷰 데이터 읽어오기
def read_review_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()] # 각 줄마다 '\t' 단위로 분리 => [id, document, label]
        data = data[1:] # 맨 첫 줄의 헤더 제거
    return data

# 학습 시간 측정 시작
start = time.time()

print('1) 말뭉치 데이터 읽기 시작')
review_data = read_review_data('./ratings.txt')
print('리뷰 데이터 개수 : ', len(review_data)) # 200000
print('1) 말뭉치 데이터 읽기 완료 : ', time.time()-start) # 0.7904026508331299

print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료 : ', time.time()-start) # 188.0876066684723

print('3) Word2Vec 모델 학습 시작')
model = Word2Vec(sentences=docs, size=200, window=4, hs=1, min_count=2, sg=1)
print('3) Word2Vec 모델 학습 완료 : ', time.time()-start) # 243.24152278900146

print('4) 학습된 모델 저장 시작')
model.save('nvmc.model')
print('4) 학습된 모델 저장 완료 : ', time.time()-start)  # 247.41529059410095

print("corpus_count : ", model.corpus_count)  # 200000
print("corpus_total_words : ", model.corpus_total_words)  # 1076896


# 모델 불러오기
# model = Word2Vec.load('nvmc.model')
# print("corpus_total_words : ", model.corpus_total_words)

# 단어 임베딩 벡터 생성
print('사랑 : ', model.wv['사랑'])

# 두 단어간의 유사도 계산
print("일요일 - 월요일\t", model.wv.similarity(w1='일요일', w2='월요일')) # 0.652986
print("송강호 - 배우\t", model.wv.similarity(w1='송강호', w2='배우')) # 0.63401085
print("대기업 - 삼성\t", model.wv.similarity(w1='대기업', w2='삼성')) # 0.5647633
print("일요일 - 삼성\t", model.wv.similarity(w1='일요일', w2='삼성')) # 0.2750886
print("빵 - 크리스마스\t", model.wv.similarity(w1='빵', w2='크리스마스')) # 0.21639587

# 가장 유사한 단어 추출
print(model.wv.most_similar("송강호", topn=5)) # [('이나영', 0.6971107721328735), ('한석규', 0.6925764083862305), ('남지현', 0.6672976613044739), ('윤제문', 0.6609833240509033), ('황우슬혜', 0.6587698459625244)]
print(model.wv.most_similar("시리즈", topn=5)) # [('캐리비안의 해적', 0.6778707504272461), ('X맨', 0.6507395505905151), ('비포 선셋', 0.6431201696395874), ('잭 라이언', 0.6403617858886719), ('더 울버린', 0.6360614895820618)]

