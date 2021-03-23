## REST API (Representational State Transfer API)
  - 웹(HTTP) URI를 통해 resource를 명시
  - HTTP 메소드(GET, POST, PUT, DELETE)를 통해 resource에 대한 CRUD 동작을 처리하는 API 호출 방식

<br>

- API 서버 구축을 위해 __Flask__ 웹 애플리케이션 프레임워크를 이용
  - 간단하고 빠르게 구축 가능

  <br><br>


### 기본 구현 방법

  <br>

```    
from flask import Flask
app = Flask(__name__) 
```
- 현재 실행되는 애플리케이션의 모듈명을 인자로 넘겨 Flask 객체 생성 

  <br>


```
@app.route('/') # 라우트
def func():  # view 함수
  return "Hello"
```
- 라우트(Route) : 호출된 URI를 처리하는 함수를 연결하는 것
- 브라우저에서 '/'라는 URI를 호출했을 때 func() 함수의 결과값이 브라우저 화면에 보이게 된다. _(그래서 view 함수라고 부름)_
- host='127.0.0.1', port='5050'이면, 'http://127.0.0.1:5000/'에 접속

  <br>

```
if __name__ == '__main__':
  app.run() # app.run(host='127.0.0.1', port='5050')
```
- 현재 파일인 app.py이 메인 모듈로 실행되는 경우에만 Flask 서버 실행

<br><br>

#### URI 동적 변수 사용하기

```
@app.route('/info/<name>')
def get_name(name):
    return "name is {}".format(name)
```

```
@app.route('/user/<int:id>')
def get_id(id):
    return "id is {}".format(id)
```

```
@app.route('/json/<int:id>/<text>')
def json_data(id, text):
    json = {
        "id": id,
        "text": text
    }
    return json
```
- URI에 지정한 데이터타입이 아닌 경우 오류 페이지 출력 (기본 데이터타입은 str)

<br><br>

#### GET, POST 메소드 사용

```
@app.route('/user/<int:id>', methods=['GET'])
...
```

```
from flask import request

@app.route('/user', methods=['POST'])
def add_user():
...
```

<br><br>

#### 자주 쓰이는 함수

```
from flask import request, jsonify
import json
```

`request.get_json()` : POST 메소드에서 HTTP 요청 body로부터 json 데이터를 불러옴<br>
`jsonify()` : json response 형태로 변환 (return 시 많이 사용)<br>
`json.dumps()` : json 객체 -> json 문자열로 변환 (서버에 전송할 때)<br>
`json.loads()` : json 문자열 -> 딕셔너리 객체로 변환 (서버에서 받아올 때)<br>


