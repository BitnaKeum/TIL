# 챗봇 서버 모듈

import socket

class BotServer:
    def __init__(self, srv_port, listen_num):   # srv_port : 생성할 소켓 서버의 포트번호, listen_num : 연결을 수락할 클라이언트 수
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None

    # 소켓 생성
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IP 소켓 생성
        self.mySock.bind(("0.0.0.0", int(self.port)))   # 소켓 서버 포트번호 지정
        self.mySock.listen(int(self.listen))            # self.listen 수 만큼 클라이언트 연결을 수락
        return self.mySock

    # 클라이언트 연결을 대기하고 있다가 연결을 수락
    def ready_for_client(self):
        return self.mySock.accept()   # (conn, address) 반환 => conn: 클라이언트 소켓 객체, address: 클라이언트 소켓의 바인드된 주소

    # 소켓 반환
    def get_sock(self):
        return self.mySock