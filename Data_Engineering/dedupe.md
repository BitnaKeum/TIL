# Dedupe

[repo](https://github.com/dedupeio/dedupe) | [참고 링크](https://docs.dedupe.io/en/latest/Matching-records.html)

### String metric

- 두 문장이 duplicate한지를 판별하기 위해 사용하는 방법
  - 유사하면 낮은 값 반환
  - 유사하지 않으면 높은 값 반환

- Hamming Distance
	- 어떤 문장을 다른 문장으로 바꿀 때 대체되는 글자의 수를 카운트
	- _ex)_ `roberts` -> `Roberts` 로 바꾸려면 `r` -> `R` 한 글자만 바꾸면 되므로 Hamming distance = 1

- __Affine Gap Distance__
	- Gap : 두 문장의 길이를 맞추기 위해 더 짧은 문장에 빈칸을 채워 넣는 것

![image](https://user-images.githubusercontent.com/37769713/130175227-b195f307-fba5-41a8-99ae-87e023b68c68.png)

  - Open : Gap이 이어진 부분의 시작점 수
  - Extension : Open을 제외한 Gap의 수

![image](https://user-images.githubusercontent.com/37769713/130175811-7a036293-336e-496b-95e6-99ceae39de41.png) 

  - Affine Gap Distance는 Open과 Extension의 Gap penalty를 이용해 계산하는 방식
  - 자세한 설명은 [여기](https://freshrimpsushi.github.io/posts/sequence-alignment-score-and-gap-penalty/)를 참고
<br>

### Setting weights and making decisions
- Record by Record 계산

![image](https://user-images.githubusercontent.com/37769713/130177698-b9345470-2185-46eb-a066-017f037a0278.png)

- Field by Field 계산

![image](https://user-images.githubusercontent.com/37769713/130177740-7aebda58-5566-478a-93f2-1bf8f7229561.png)

- Record by Record 또는 Field by Field로 계산한 record distance 값이 duplicate를 의미하는 건지 distinct를 의미하는 건지 모호하다는 문제점
- duplicate인지 distinct인지 레이블링을 해둔 문장 쌍을 넣어주어, regularized logistic regression를 통해 모델이 weight set을 학습하도록 하여 해결

