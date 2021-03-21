# 챗봇 엔진 서버 메인 프로그램

import threading
import json

from config.DatabaseConfig import *
from utils.Database import Database
from utils.BotServer import BotServer
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel
from models.ner.NerModel import NerModel
from utils.FindAnswer import FindAnswer

# 전처리 객체 생성
p = Preprocess(word2index_dic='train_tools/dict/chatbot_dict.bin', userdic='utils/user_dic.tsv')

# 의도 파악 모델
intent = IntentModel(model_name='models/intent/intent_model.h5', proprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='models/ner/ner_model.h5', proprocess=p)

def to_client(conn, addr, params):  # 스레드 함수
    db = params['db']

    try:
        db.connect()    # DB 연결

        # 데이터 수신
        read = conn.recv(2048)  # 수신 데이터가 있을 때까지 블로킹, 최대 2048바이트의 데이터 수신
        print("===========================")
        print("Connection from: %s" % str(addr))

        if read is None or not read:    # 클라이언트 연결이 끊어지거나 오류가 있는 경우
            print("클라이언트 연결 끊어짐")
            exit(0) # 스레드 강제 종료

        # json 데이터로 변환 (클라이언트가 서버 쪽으로 요청한 것)
        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']

        # 의도 파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]

        # 개체명 파악
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        # 답변 검색
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)
        except:
            answer = "죄송해요 무슨 말인지 모르겠어요. 조금 더 공부할게요."
            answer_image = None

        # 서버 -> 클라이언트로 응답하는 JSON 객체
        send_json_data_str = {
            "Query" : query,
            "Answer" : answer,
            "AnswerImageUrl" : answer_image,
            "Intent" : intent_name,
            "NER" : str(ner_predicts)
        }
        message = json.dumps(send_json_data_str)   # 소켓 통신에서 객체 형태로는 데이터 송신이 불가하므로 문자열로 변환
        conn.send(message.encode())  # UTF-8로 인코딩하여 클라이언트에 응답 전송

    except Exception as ex:
        print(ex)

    finally:
        if db is not None:
            db.close()  # DB 연결 해제
        conn.close()


if __name__ == '__main__':
    # 질문/답변 학습 DB 연결 객체 생성
    db = Database(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME)
    print("DB 접속")

    # 봇 서버 동작
    port = 5050
    listen = 100
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")

    while True:   # 무한루프를 돌면서 클라이언트의 연결을 기다림
        # 클라이언트의 서버 연결 요청이 수락되는 즉시 클라이언트의 서비스 요청을 처리할 수 있는 스레드 생성
        conn, addr = bot.ready_for_client()
        params = {
            'db': db
        }

        client = threading.Thread(target=to_client, args=(
            conn,
            addr,
            params
        ))  # 생성된 스레드는 to_client() 함수를 호출
        client.start()  # 스레드 시작