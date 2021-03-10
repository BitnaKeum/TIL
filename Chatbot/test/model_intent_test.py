from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin', userdic='../utils/user.dic.tsv')

intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)
query = "떡볶이 좀 시키려고 하는데요"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)