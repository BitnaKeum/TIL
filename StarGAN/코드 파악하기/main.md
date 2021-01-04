




![image](https://user-images.githubusercontent.com/37769713/103545292-b3bdc300-4ee4-11eb-8727-8714a0ed71bc.png)


mode에 'train'를 적었으면 solver.py에 정의된 train() 함수를 실행하고,

mode에 'test'를 적었으면 solver.py에 정의된 test() 함수를 실행한다.

<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545337-c2a47580-4ee4-11eb-895c-6a97cef01ca5.png)


c_dim은 데이터셋에서 사용할 특성(attribute)의 수를 의미한다.

(StarGAN에서 기본적으로 CelebA 데이터셋으로부터 'Black_Hair', 'Blond_Hair', 'Brown_Hair', 'Male', 'Young' 특성을 사용하기 때문에 default값이 5이다)


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545365-cc2ddd80-4ee4-11eb-9060-2b4deb6fd4bc.png)


image_size는 모델에 들어갈 이미지의 크기를 의미한다. default는 128x128이다.


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545389-d8199f80-4ee4-11eb-95f2-14eb65c60da2.png)


![image](https://user-images.githubusercontent.com/37769713/103545421-e1a30780-4ee4-11eb-8622-0b8617bb9d7d.png)


![image](https://user-images.githubusercontent.com/37769713/103545457-ebc50600-4ee4-11eb-9ec2-5b0ecb2d7327.png)



g_conv_dim은 Generator 구조에서 첫번째 layer의 filter 수를 의미한다. 논문을 따라 default는 64이다.

g_repeat_num은 Generator 구조에서 Residual Block의 수를 의미한다. 논문을 따르면 default는 6이다.


<br><br>



![image](https://user-images.githubusercontent.com/37769713/103545498-fda6a900-4ee4-11eb-9d8b-56978540cc26.png)


![image](https://user-images.githubusercontent.com/37769713/103545514-05664d80-4ee5-11eb-9fdf-da0c00885a4b.png)


![image](https://user-images.githubusercontent.com/37769713/103545532-0c8d5b80-4ee5-11eb-9516-9e5b64434eca.png)


 d_conv_dim은 Discriminator 구조에서 첫번째 layer의 filter 수를 의미한다. 논문에 따르면 default는 64이다.

d_repeat_num은 Discriminator 구조에서 Output layer를 제외한 convolution layer의 수이다. 논문에 따르면 default는 6이다.


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545572-1616c380-4ee5-11eb-917d-f7e8fca8e4e9.png)


![image](https://user-images.githubusercontent.com/37769713/103545602-1f079500-4ee5-11eb-9295-536ee7e65976.png)



lambda_gp는 adversarial loss를 구하는 데에 사용되는 gradient penalty 값을 의미하며 default는 10이다.

<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545627-2890fd00-4ee5-11eb-8d12-cefb4be2a337.png)


num_iters는 학습 과정에서 몇 번의 iteration을 돌 것인지를 나타내는 값이다. default로 200000번의 iteration을 수행한다.


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545646-30e93800-4ee5-11eb-9db5-074d90b501b1.png)


![image](https://user-images.githubusercontent.com/37769713/103545675-3d6d9080-4ee5-11eb-9086-1cdd3e41ad2c.png)



n_critic은 Discriminator가 몇 번 update되었을 때 Generator를 한번 update시킬 것인지를 의미하는 값이다. 

<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545705-465e6200-4ee5-11eb-86c4-f3c399ed3031.png)



selected_attrs는 CelebA 데이터셋에서 사용할 특성들이다.

default로는 'Black_Hair', 'Blond_Hair', 'Brown_Hair', 'Male', 'Young' 특성이 사용된다. 


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545726-5118f700-4ee5-11eb-869f-7dd725bb63c8.png)



test_iters는 모델 테스트를 위해 학습된 모델을 몇 번째 step에서 가져올 것인지를 의미한다.

다시 말해, 모델 학습 시에 model_save_step 인자의 default 값인 10000번째 iteration마다 학습 모델이 저장되는데, 몇 번째 iteration에서 저장된 학습 모델을 가져와 테스트를 할 것인지를 나타내는 값이다.

(num_iters의 default가 200000이기 때문에 test_iters의 default도 200000이다)


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545773-62fa9a00-4ee5-11eb-8fa4-868e50dc4e8c.png)


num_workers는 몇 개의 CPU 코어를 할당할 것인지를 나타내는 값이라고 한다.

좀 개념이 어려워서 jybaek.tistory.com/799에 잘 설명되어 있으니 참고하면 좋을 것 같다.

default는 1이지만 github.com/yunjey/stargan/issues/43와 같은 에러가 발생하는 경우 값을 0으로 설정하는게 도움이 될 수도 있다.

<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545822-7443a680-4ee5-11eb-9e2a-f425a80249f8.png)



mode는 train을 할 것인지 test를 할 것인지를 결정하는 값이다. 

<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545838-7d347800-4ee5-11eb-99e9-a60838de90dc.png)



CelebA 데이터셋을 사용하는 경우 데이터셋이 저장되는 default 경로는 'data/celeba/images'이다.

CelebA를 사용하면 attribute 정보를 담고 있는 list_attr_celeba.txt 파일도 만들어줘야 하는데, 이 파일이 위치하는 경로를 attr_path에 써준다.

<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545862-84f41c80-4ee5-11eb-94cb-8c8369b4007a.png)


RaFD 데이터셋을 사용하는 경우 학습용 데이터셋이 저장되는 default 경로는 'data/RaFD/train'이다.

'train' 폴더 하위에 특성별로 폴더를 만들어 그 안에 이미지를 저장해야한다.


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545896-8faeb180-4ee5-11eb-88cb-31d38ce1360d.png)



model_save_dir은 모델 학습 과정에서 model_save_step 인자 값에 해당하는 iteration 수마다 학습 모델이 저장되는 경로이다.

10000-D.ckpt, 10000-G.ckpt 형태의 모델들이 저장된다.


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545916-989f8300-4ee5-11eb-941f-13af25c53b47.png)


result_dir은 모델 테스트 결과가 저장되는 경로이다.

테스트 데이터셋을 각각의 특성으로 합성된 이미지들이 저장된다.


<br><br>


![image](https://user-images.githubusercontent.com/37769713/103545970-a8b76280-4ee5-11eb-9221-01f4465b95a6.png)


model_save_step은 모델 학습 과정에서 몇 번째 iteration마다 학습 모델을 저장할 것인지를 나타낸다.

default가 10000이므로 10000번째, 20000번째, ... 학습 모델들이 저장된다.



