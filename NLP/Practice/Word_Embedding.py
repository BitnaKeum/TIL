from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()
text = "오늘 날씨는 구름이 많아요."


########## one-hot 인코딩 ##########

# 명사 추출
nouns = komoran.nouns(text)
print(nouns)  # ['오늘', '날씨', '구름']

# 단어사전 구축 및 인덱스 부여
dic = {}
for noun in nouns:
    if noun not in dic.keys():
        dic[noun] = len(dic)
print(dic)  # {'오늘': 0, '날씨': 1, '구름': 2}

# one-hot 인코딩
dim = len(dic)
index = list(dic.values())
one_hot_index = np.eye(dim)[index]
print(one_hot_index)  # [[1. 0. 0.]
                      #  [0. 1. 0.]
                      #  [0. 0. 1.]]

#####################################

