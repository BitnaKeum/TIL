
## 리스트(List)

`lis = [3, 5, 1, 4]`

<br>

#### 정렬하기
`lis.sort()    # [1, 3, 4, 5]`

<br>

#### 길이 구하기
`len(lis)   # 4`

<br><br>




## 튜플(Tuple)


#### 매개변수에 * 표시
나머지 매개변수들을 하나의 튜플로 묶음
```
def func(num1, num2, *rest):
...
```

```
func(1, 2, 3, 4, 5, 6)  # num1 = 1, num2 = 2, rest = (3,4,5,6)
```

<br>

#### 튜플 -> 리스트
```
tup = (1, 2, 3)
lis = list(tup)   # [1, 2, 3]
```

<br>

#### 리스트 -> 튜플
```
lis = [1, 2, 3]
tup = tuple(lis)  # (1, 2, 3)
```

<br><br>





## 딕셔너리(Dictionary)

#### 선언 방법
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

#### 원소 삭제 방법
`del dic['yellow']`

<br>

#### 딕셔너리 -> 리스트

```
dic = {'red':'apple', 'yellow':'banana'}
list_key = dic.keys()       # ['red', 'yellow']
list_value = dic.values()   # ['apple', 'banana']
```

<br><br>


## lambda 표현식

#### 사용 방법
`lambda 인자 : 표현식`

<br>

`(lambda x : x + 10)(10)    # 20`

<br>

#### map()
`map(함수, 리스트)`

리스트로부터 원소를 하나씩 꺼내 함수를 적용하고, 결과값을 모두 담은 리스트를 반환한다.

<br>

`map(lambda x : x + 10, [10, 20, 30])   # [20, 30, 40] `


<br><br>



####
