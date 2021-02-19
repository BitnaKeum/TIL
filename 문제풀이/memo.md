
## 윤년, 평년

윤년 : 2월 29일 O<br>
평년 : 2월 29일 X<br>
<br>
연도가 4로 나누어 떨어지면 => 윤년<br>
연도가 4, 100으로 나누어 떨어지면 => 평년<br>
연도가 4, 100, 400로 나누어 떨어지면 => 윤년<br>

<br><br><br>



## 정수 입력 받기

1개 : `num = int(input())` <br>
2개 : `num1, num2 = map(int, input().split())` <br>

<br><br><br>



## Slicing

- 리스트 슬라이싱 결과 값은 리스트형
- 실제 범위를 벗어나도 에러가 발생하지 않음!
```
lis = [2,4,6,8]
lis[3:6]  # [8]
```

<br><br><br>


# collections

### defaultdict
- default 값을 설정하여 딕셔너리를 생성
- 어떤 조건을 만족하면 특정 key의 value를 증가시키는 경우 유용하게 사용

```
dic = collections.defaultdict(int)  # default 값 : 0
dic['A'] += 1 # 원래대로라면 존재하지 않는 key 값이므로 에러가 발생하지만, {'A': 1}이 됨
```

<br><br>

### Counter
- 시퀀스 객체에서 각 값의 빈도 수를 세서 딕셔너리로 반환

#### 데이터 빈도 세기
`lis = ['a', 'b', 'b', 'c', 'b']`<br>

기본 : `collections.Counter(lis)   # Counter({'b': 3, 'a': 1, 'c': 1})`<br>
빈도 높은 순(모두) : `collections.Counter(lis).most_common()   # [('b', 3), ('a', 1), ('c', 1)]`<br>
빈도 높은 순(2개만)  : `collections.Counter(lis).most_common(2)  # [('b', 3), ('a', 1)]`<br>

<br>

#### 한 시퀀스 자료형에서 다른 시퀀스 자료형과 겹치지 않는 원소 찾기

```
lis1 = ['a', 'b', 'c']
lis2 = ['b', 'c', 'd']
result = Counter(lis1) - Counter(lis2)    # Counter({'a': 1})
list(result.keys())   # ['a']
```

<br><br>

### OrderedDict
- 딕셔너리의 입력 순서를 유지
- Python 3.7 이상부터는 자동으로 입력 순서가 유지되지만, 혹시 모를 상황을 위해 사용하자.

`collections.OrderedDict({'c': 1, 'a': 5, 'b': 4}) # 딕셔너리 형태 유지`

<br><br><br>



## 리스트 -> 문자열
`''.join(리스트)`

<br><br><br>


## 문자열 정렬하기
- sorted() 함수로 정렬된 리스트를 얻은 후, 이를 문자열로 바꾸기 위해 join() 함수를 사용
```
s = "apple"
s_sort = sorted(s) # [a, e, l, p, p]
''.join(s_sort)   # "aelpp"
```

<br><br><br>

## 진법 변환하기
`int(변환할 수 문자열, 진법)`

ex) `int('1010', 2)   # 10`

<br><br><br>

## 소수 찾기
제일 먼저 2로 나누어 떨어지는지 확인한 후,  3부터 2씩 건너뛰면서 확인한다 (for 효율성)

<br><br><br>

## 문자가 알파벳/숫자인지 확인
`ch.isalnum() # True/False`

<br><br><br>
