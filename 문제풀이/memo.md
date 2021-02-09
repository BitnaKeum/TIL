
## 윤년, 평년

윤년 : 2월 29일 O<br>
평년 : 2월 29일 X<br>
<br>
연도가 4로 나누어 떨어지면 => 윤년<br>
연도가 4, 100으로 나누어 떨어지면 => 평년<br>
연도가 4, 100, 400로 나누어 떨어지면 => 윤년<br>

<br><br>


## Slicing

- 리스트 슬라이싱 결과 값은 리스트형
- 실제 범위를 벗어나도 에러가 발생하지 않음!
```
lis = [2,4,6,8]
lis[3:5]  # [8]
```

<br><br>


## Counter 클래스

`from collections import Counter  # 내장되어있음`
<br>
`Counter(시퀀스 자료형)` <br><br>

#### 데이터 개수 세기
`Counter(['a', 'b', 'b', 'c', 'b'])   # Counter({'a': 1, 'b': 3, 'c': 1})`<br>

#### 데이터 개수 세기 (빈도 높은 순)
`lis = ['a', 'b', 'b', 'c', 'b']`
모든 문자에 대해 : `Counter(lis).most_common()   # [('b', 3), ('a', 1), ('c', 1)]`<br>
2개 문자에 대해  : `Counter(lis).most_common(2)  # [('b', 3), ('a', 1)]`<br>

#### 한 시퀀스 자료형에서 다른 시퀀스 자료형과 겹치지 않는 원소 찾기

```
lis1 = ['a', 'b', 'c']
lis2 = ['b', 'c', 'd']
result = Counter(lis1) - Counter(lis2)    # Counter({'a': 1})
list(result.keys())   # ['a']
```
<br>

