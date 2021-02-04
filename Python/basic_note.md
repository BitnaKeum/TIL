## Iterable 자료형

### 리스트(List)

`lis = [3, 5, 1, 4]`

<br>

정렬하기 : `lis.sort()    # [1, 3, 4, 5]` <br>
길이 구하기 : `len(lis)   # 4` <br>
끝에서 3번째 원소부터 마지막 원소까지 출력 : `lis[-3:]` <br>

<br>

리스트 -> 문자열
`''.join(lis)` => 각 원소를 공백 없이 이어 붙이기 <br>   
`' '.join(lis)` => 각 원소를 공백과 함께 이어 붙이기 <br>

<br><br><br>


### 튜플(Tuple)


매개변수에 * 표시 => 나머지 매개변수들을 하나의 튜플로 묶음
```
def func(num1, num2, *rest):
...
```

```
func(1, 2, 3, 4, 5, 6)  # num1 = 1, num2 = 2, rest = (3,4,5,6)
```

<br>

튜플 -> 리스트
```
tup = (1, 2, 3)
lis = list(tup)   # [1, 2, 3]
```

<br>

리스트 -> 튜플
```
lis = [1, 2, 3]
tup = tuple(lis)  # (1, 2, 3)
```

<br><br><br>



### 딕셔너리(Dictionary)

선언 방법
```
dic = {}
dic['red'] = 'apple'
dic['yellow'] = 'banana'
```
or
```
dic = {}
dic = {'red':'apple', 'yellow':'banana'}
```

<br>

원소 삭제 방법
`del dic['yellow']`

<br>

딕셔너리 -> 리스트

```
dic = {'red':'apple', 'yellow':'banana'}
list_key = dic.keys()       # ['red', 'yellow']
list_value = dic.values()   # ['apple', 'banana']
```

<br><br><br>


### 집합(Set)

```
set([1,2,3])      # {1, 2, 3}
set("Hello")      # {'l', 'e', 'o', 'H'}
```
<br>
- 중복 불가<br>
- 순서 없음<br>
<br>
값 1개 추가 : `s.add(4)` <br>
값 여러 개 추가 : `s.update([4,5,6])` <br>
값 제거 : `s.remove(1)` <br>

<br>

### sorted() 함수

`sorted(iterable 자료형)`<br>
- 오름차순 정렬하여 리스트로 반환한다 (리스트의 sort() 함수와 구분하기)<br>



<br><br><hr><br>


## 문자열

### 텍스트 문자열(Text String)

`text_str = ' Hello '`
<br>

맨 앞/뒤의 공백 제거 : `text_str.strip()  # 'Hello'`<br>
텍스트 대체 : `text_str.replace(기존 문자열, 대체할 문자열)`<br>

<br>

### 바이트 문자열(Byte String)

`byte_str = b'Hello'`
<br>
텍스트 문자열 -> 바이트 문자열 : `text_str.encode('utf-8')`<br>
바이트 문자열 -> 텍스트 문자열 : `byte_str.decode('utf-8')`<br>

<br>

### 원시 문자열(Raw String)

`raw_str = r'C:\Users'    # 백슬래시를 해석하지 않음`
<br>
파일 경로, 정규 표현식에서 유용하게 사용

<br><br>

### f 문자열

포맷을 갖는 문자열
```
name = 'maru'
age = 1
avg = 99.9
f_str = f'{name:5s age:5d avg:5.1f}'
```


<br><br><hr><br>


## 반복문

```
lis = ['red', 'blue', 'green']
```

<br>

```
for i in range(3):       # i : 0 / 1 / 2
...
```

```
for i in range(lis):     # i : 'red' / 'blue' / 'green'
...
```

```
for i, val in enumerate(lis):     # i, val : 0, 'red' / 1, 'blue' / 2, 'green'
...
```
<br><br>

### range()

간격 띄우기<br>
`list(range(1, 10, 2))      # 1, 3, 5, 7, 9`<br><br>

역순 범위<br>
`list(range(5, 0, -1))      # 5, 4, 3, 2, 1`<br>


<br><br><hr><br>


## 파일 입출력

열기 : `f = open(파일 경로, 모드)   # 모드를 안 써주면 읽기 모드(r)로 열음`<br>
읽기 : `f.read()`<br>
쓰기 : `f.write(쓸 내용)   # f.close()까지 해줘야 실제 파일이 업데이트됨!!`<br>
닫기 : `f.close()`<br><br>

한 줄 읽기 : `f.readline()`<br>
파일 전체를 한 줄씩 읽어서 배열에 저장 : `f.readlines()`<br>


<br><br><hr><br>


## lambda 표현식

### 사용 방법
`lambda 인자 : 표현식`

<br>

`(lambda x : x + 10)(10)    # 20`

<br>

### map()
`map(함수, Iterable 자료형)`

- Iterable 자료형에서 원소를 하나씩 꺼내 함수를 적용하고, 결과값을 모두 담아 반환한다.

<br>

`list(map(lambda x : x + 10, [10, 20, 30]))   # [20, 30, 40] `


<br><br><hr><br>


## 모듈 

### 모듈 불러오기

1. `import 모듈명`
=> 모듈 내 변수를 사용하려면 모듈명.변수 형태로 사용해야함(번거로움)
<br>

2. `from 모듈명 import *`
=> 이름만으로 사용이 가능함. But 기존 코드에 있는 변수명이 해당 모듈에도 있을 경우, 값이 뜻하지 않게 변할 수 있음
<br><br>

### 모듈 다시 불러오기
`reload(모듈명)` => 모듈의 코드가 수정된 경우 다시 불러온다


<br><br>

### random 모듈

`random.random()` => 0 이상 1 미만의 난수를 생성<br>

`random.randrange(1,6)` => 1 이상 6 미만의 정수 난수를 생성<br>

`random.shuffle(순서형자료)` => 섞어줌<br>


<br><br><hr><br>


## 클래스, 메소드

### 기본 사용 방법

```
# 파일명 : Info.py
class Student:
    kor = 90
    mat = 100
    eng = 95

    def __init__(self):
        print("학생이 추가되었습니다.")

    def Grade(self):
        return 'A'
```

```
import Info

bitna = Info.Student()  # '학생이 추가되었습니다.'
bitna.math      # 100
bitna.Grade()   # 'A'
```
<br>

- 메소드 정의 시 항상 인자에 self를 써준다!<br><br>


### __init__ 메소드 (생성자)

```
def __init__(self, 인자):   # 인자 생략 가능
...
```

<br>
- 해당 클래스 객체를 생성하면 자동으로 실행되어 초기화를 진행한다

<br><br>

### 상속(Inheritance)

- 클래스의 인자에 상속할 클래스를 써준다!


```
class Bitna(Student):  # Bitna Class는 Student Class를 상속 받는다
  def major(self):
    return 'Computer Engineering'
```

<br><br>
