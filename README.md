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
![input](https://user-images.githubusercontent.com/94462842/169660224-57faf285-40d3-469f-a8c5-dcc0373caf16.PNG)

  
* pre-trained 데이터셋을 바탕으로 cnn 처리된 이미지    
![out](https://user-images.githubusercontent.com/94462842/169660228-c1340bc7-8526-42a7-8384-b21ed8024f7a.PNG)

  
* 콘솔 output    
![console](https://user-images.githubusercontent.com/94462842/169660233-0ec124e1-25b8-4a20-9154-b7e38c2eddca.PNG)


* Firestore DB로 결과값 저장    
![db](https://user-images.githubusercontent.com/94462842/169660234-e6b0ac0b-c0bd-48b2-9255-bc9a421c91dd.PNG)

  

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
