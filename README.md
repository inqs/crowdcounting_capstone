# crowdcounting_capstone
INU Capstone Project '21-'22  
  
학식 도우미 프로젝트 https://github.com/junsick3265/haksikhelper  
크라우드 카운팅 부분  
  
## Tools used
* python 3.10.3  
* opencv 4.5.5  
* Firebase
* Pycharm  
* Caffe2 dataset
* Raspberry Pi 4 w/ camera module

## Preparing Input  
* 라즈베리파이를 이용하여 설정한 시간 간격마다 이미지를 촬영하여 실시간으로 Firebase Storage에 업로드  
![pi_setup](https://user-images.githubusercontent.com/94462842/160591361-198dc285-7164-48d2-a8bf-3fe84e0ac007.PNG)  
  
## Output  
* input 사진    
  <img src="https://user-images.githubusercontent.com/94462842/160598324-906ab847-34fe-4fc4-8ce0-6933f6564c1a.PNG" width="500" height="500">  
  
* pre-trained 데이터셋을 바탕으로 cnn 처리된 이미지    
![res_img](https://user-images.githubusercontent.com/94462842/160594072-227b05cb-0aee-44b8-85c2-b47950c6de3c.PNG)  
  
* 콘솔 output    
![result](https://user-images.githubusercontent.com/94462842/160594112-43411239-a13d-48ac-8152-475f56a89686.PNG)  

* Firestore DB로 결과값 저장    
![firestore](https://user-images.githubusercontent.com/94462842/160594172-329148fd-e338-4b7d-9008-b01afbeee4ca.PNG)  
  

## 출처  
상하이공과대학 Crowd Counting caffe model dataset 사용  
```
@inproceedings{zhang2016single,
  title={Single-image crowd counting via multi-column convolutional neural network},
  author={Zhang, Yingying and Zhou, Desen and Chen, Siqin and Gao, Shenghua and Ma, Yi},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={589--597},
  year={2016}
}
```
