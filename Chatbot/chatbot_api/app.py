from flask import Flask, request, jsonify, abort
import socket
import json

# 챗봇 엔진 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050         # 챗봇 엔진 서버 통신 포트번호

# Flask 애플리케이션  (Python 웹 애플리케이션 프레임워크)
app = Flask(__name__)   # 현재 실행되는 애플리케이션의 모듈명 전달

# 챗봇 엔진 서버와 통신
def get_answer_from_engine(bottype, query):
    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': bottype
    }
    message = json.dumps(json_data) # json 객체를 json 문자열로 변환
    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)     # json 문자열을 딕셔너리 객체로 반환

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data

# 챗봇 엔진 query 전송 API
@app.route('/query/<bot_type>', methods=['POST'])
def query(bot_type):
    body = request.get_json()   # HTTP body의 json 데이터를 딕셔너리 형태로 가져옴

    try:
        if bot_type == 'TEST':
            # 챗봇 API 테스트
            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret) # json response 형태로 반환

        elif bot_type == 'KAKAO':
            # 카카오톡 처리 (10장에서 구현)
            pass

        elif bot_type == 'NAVER':
            # 네이버톡톡 처리 (11장에서 구현)
            pass

        else:
            abort(404)  # 정의되지 않은 bot type인 경우 404 오류

    except Exception as ex:
        abort(500)  # 에러 발생 시 500 오류


if __name__ == '__main__':
    app.run()


