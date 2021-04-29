
# 데이터셋 읽어오기
dat <- read.csv(file="C:/Users/beaus/Desktop/google_review_ratings.csv", header=TRUE)
head(dat)

# 필요없는 열 삭제
dat <- subset(dat, select=-c(User, X))

# 열 이름 변경
names(dat)
names(dat) <- c("Church", "Resort", "Beach", "Park", "Theater", "Museum", "Mall", "Zoo", "Restaurant", "Bar", "Local_service", "Fastfood_shop", "Hotel", "Juice_bar", "Gallery", "Club", "Swimming_pool", "Gym", "Bakery", "Spa", "Cafe", "Viewpoint", "Monument", "Garden")

# 데이터 타입 numeric으로 변경
dat$Local_service <- as.numeric(dat$Local_service)

# 표준화(Standardization)
dat <- transform(dat, Church=scale(Church), Resort=scale(Resort), Beach=scale(Beach), Park=scale(Park), Theater=scale(Theater), Museum=scale(Museum), Mall=scale(Mall), Zoo=scale(Zoo), Restaurant=scale(Restaurant), Bar=scale(Bar), Local_service=scale(Local_service), Fastfood_shop=scale(Fastfood_shop), Hotel=scale(Hotel), Juice_bar=scale(Juice_bar), Gallery=scale(Gallery), Club=scale(Club), Swimming_pool=scale(Swimming_pool), Gym=scale(Gym), Bakery=scale(Bakery), Spa=scale(Spa), Cafe=scale(Cafe), Viewpoint=scale(Viewpoint), Monument=scale(Monument), Garden=scale(Garden))

# 정규화(Normalization) 함수 정의
normalize <- function(x) {
  return((x-min(x))/(max(x)-min(x)))
}
# 정규화 => 0~1
dat <- transform(dat, Church=normalize(Church), Resort=normalize(Resort), Beach=normalize(Beach), Park=normalize(Park), Theater=normalize(Theater), Museum=normalize(Museum), Mall=normalize(Mall), Zoo=normalize(Zoo), Restaurant=normalize(Restaurant), Bar=normalize(Bar), Local_service=normalize(Local_service), Fastfood_shop=normalize(Fastfood_shop), Hotel=normalize(Hotel), Juice_bar=normalize(Juice_bar), Gallery=normalize(Gallery), Club=normalize(Club), Swimming_pool=normalize(Swimming_pool), Gym=normalize(Gym), Bakery=normalize(Bakery), Spa=normalize(Spa), Cafe=normalize(Cafe), Viewpoint=normalize(Viewpoint), Monument=normalize(Monument), Garden=normalize(Garden))

# 결측치 제거
dat <- subset(dat, select=-c(Local_service, Fastfood_shop, Garden))

# bar plot 출력
dat_mall = c(dat$Mall)
barplot(dat_mall)

# scatter plot 출력
#qplot(dat$Restaurant, dat$Bar)
qplot(Restaurant, Bar, data=dat)

# pie chart 출력
dat <- dat*10
dat <- round(dat)
val1 = nrow(dat[dat$Park == 1,])
val2 = nrow(dat[dat$Park == 2,])
val3 = nrow(dat[dat$Park == 3,])
val4 = nrow(dat[dat$Park == 4,])
val5 = nrow(dat[dat$Park == 5,])
val5 = nrow(dat[dat$Park == 6,])
val5 = nrow(dat[dat$Park == 5,])
val6 = nrow(dat[dat$Park == 6,])
val7 = nrow(dat[dat$Park == 7,])
val8 = nrow(dat[dat$Park == 8,])
val9 = nrow(dat[dat$Park == 9,])
val10 = nrow(dat[dat$Park == 10,])
val = c(val1, val2, val3, val4, val5, val6, val7, val8, val9, val10)
pie(val)


# 선형회귀 모델 생성
multi_linear <- lm(Park ~ ., data = dat)
summary(multi_linear)

# 히스토그램 출력
hist(dat$Park)

# error 값들 출력
library(forecast)
accuracy(multi_linear)


# 로지스틱회귀 모델 생성
model_logit <- glm(Park ~ ., data = dat, family = quasibinomial())
summary(model_logit)

# Confusion matrix
cm <- table(pred=pred_class, actual=dat_test$Park)

# 평가 지표 출력
perf_eval <- function(cm){
  # true positive rate
  TPR = Recall = cm[2,2]/sum(cm[2,])
  # precision
  Precision = cm[2,2]/sum(cm[,2])
  # true negative rate
  TNR = cm[1,1]/sum(cm[1,])
  # accuracy
  ACC = sum(diag(cm)) / sum(cm)
  # balance corrected accuracy (geometric mean)
  BCR = sqrt(TPR*TNR)
  # f1 measure
  F1 = 2 * Recall * Precision / (Recall + Precision)
  
  re <- data.frame(TPR = TPR,
                   Precision = Precision,
                   TNR = TNR,
                   ACC = ACC,
                   BCR = BCR,
                   F1 = F1)
  return(re)
}
perf_eval(cm)


# p-value가 유의하지 않은 변수 제거 (Bar, Spa, Hotel)
model_linear <- lm(Park ~ Church+Resort+Beach+Theater+Museum+Mall+Zoo+Restaurant+Juice_bar+Gallery+Club+Swimming_pool+Gym+Bakery+Cafe+Viewpoint+Monument, data = dat)
model_logit <- glm(Park ~ Church+Resort+Beach+Theater+Museum+Mall+Zoo+Restaurant+Juice_bar+Gallery+Club+Swimming_pool+Gym+Bakery+Cafe+Viewpoint+Monument, data = dat)
