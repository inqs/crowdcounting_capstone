from picamera import PiCamera
from time import sleep
import datetime
import sys, os
import requests
import firebase_admin
from firebase_admin import credentials, storage
from uuid import uuid4
import schedule

#프로젝트 ID
PROJECT_ID = "picamera-test"

#firebase 키
cred = credentials.Certificate("/home/pi/Downloads/picamera-test-firebase-adminsdk-4clhg-6b8d8014cd.json")
default_app = firebase_admin.initialize_app(cred,{'storageBucket':f"picamera-test.appspot.com"})
#버킷\
bucket = storage.bucket()

def imgUpload(file):
    blob = bucket.blob('image_store/'+file) #파이어베이스 스토리지 image_store디렉토리에 저장
    #토큰 metadata 설정
    new_token = uuid4()
    metadata = {"firebaseStorageDownloadTokens": new_token} #access token
    blob.metadata = metadata
 
    #이미지 업로드
    blob.upload_from_filename(filename='/home/pi/image_store/'+file, content_type='image/jpg') #파일이 저장된 주소와 이미지 형식(jpeg도 됨)
    #debugging hello
    print("photo taken")
    print(blob.public_url)
 
def take_photo():

    #중복없는 파일명(시간 바탕으로)
    # filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
    filename = 'image.jpg'


    #해상도 설정
    camera = PiCamera()
    #camera.resolution = (640, 480)
    #camera.resolution = (1280, 720)
    camera.resolution = (1920, 1080)
    camera.start_preview()

    sleep(5)
    #사진 저장
    camera.capture('/home/pi/image_store/' + filename)
    #파이어베이스에 업로드
    imgUpload(filename)

    camera.stop_preview()
    camera.close()
 
#10초 마다 실행
schedule.every(10).seconds.do(take_photo)
#10분에 한번씩 실행
#schedule.every(10).minutes.do(execute_camera)
#매 시간 마다 실행
#schedule.every().hour.do(clearPhoto)

 
while True:
    schedule.run_pending()
    sleep(1)
 