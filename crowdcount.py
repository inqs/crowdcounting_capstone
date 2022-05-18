import numpy as np
import cv2
from cv2 import dnn
import pylab
import matplotlib.pyplot as plt
import time
import threading
import firebase_admin
from firebase_admin import credentials, storage, firestore


#pre-trained된 모델 경로
model_path = 'model\\'

if __name__ == "__main__":

    # firebase 키
    cred = credentials.Certificate("picamera-test-firebase-adminsdk-4clhg-e41ffb9866.json")
    app = firebase_admin.initialize_app(cred, {'storageBucket': f"picamera-test.appspot.com"})
    db = firestore.client()

    while (True):
        #저장소 access
        bucket = storage.bucket()
        blob = bucket.get_blob('image_store/image.jpg')  # blob
        arr = np.frombuffer(blob.download_as_string(), np.uint8)  # array of bytes

        img_ori = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)  # Firebase에서 불러온 사진


        # cv2.imshow('image', img)
        # cv2.waitKey(0)
        #
        # #local image 사용
        # #계산하고자 하는 이미지
        # img = r'image\abcd.jpg'
        # img_ori = cv2.imread(img)
        #
        # # 테스트용 원본이미지 출력
        # plt.figure(1)
        # plt.imshow(img_ori)
        # plt.axis('off')
        # pylab.show()


        #RGB값 일부를 제외시켜 이미지 처리를 용이하게 함
        blob = dnn.blobFromImage(img_ori, 1, (1024, 768), (0, 0, 0), True)

        current = time.localtime()

        print("==============================")
        print("현재 시각:", "%04d/%02d/%02d %02d:%02d:%02d" % (current.tm_year, current.tm_mon, current.tm_mday, current.tm_hour, current.tm_min, current.tm_sec)
    )
        #이미지 네트워크가 담긴 prototxt와 protxt 데이터를 학습시킨 caffemodel을 참조
        net = dnn.readNetFromCaffe(model_path + 'mcnn_model.prototxt', model_path + 'mcnn_model.caffemodel')

        t = time.time()
        net.setInput(blob)
        density = net.forward()
        elapsed = time.time() - t

        print('이미치 처리 소요 시간: %.4f 초' % elapsed)

        density = density/1000.0
        crowd_count = np.sum(density[:])        #계산된 군중 수

        print("계산된 인원 수: ", int(crowd_count))

        # firestore에 데이터 추가
        data = {u'count': int(crowd_count), u'time': firestore.SERVER_TIMESTAMP}
        doc_ref = db.collection(u'counting').document()
        doc_ref.set(data, merge=True)



        # #테스트용 이미지 출력 (images w/ dots)
        # plt.figure(1)
        # plt.imshow(density[0, 0, :, :])
        # plt.axis('off')
        # pylab.show()

        #()초마다 반복
        time.sleep(10)