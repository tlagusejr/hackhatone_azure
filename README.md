# hackhatone_azure

 fastapi를 활용한 서버 제작입니다. 

 upload.py로 이미지 파일을 업로드, trainer.py로 학습, inference.py로 간단하게 inference학습가능합니다.

 main.py로 fastapi로 간단하게 서버를 만들고, 안에 있는 inference를 통해 http통신을 테스트 할 수 있습니다.


![image](https://user-images.githubusercontent.com/52907198/166167720-09b5acfd-ed8c-4536-8151-e317017a5071.png)

목표: 
환경:1.안드로이드 앱 
2. fastapi 서버(azure vm)
3. azure customvision
모델은 작물을 구별하는 모델, 작물의 질병을 구별하는 모델 2가지로 분리하며, 여러가지 데이터 증강 기법을 실험할 
