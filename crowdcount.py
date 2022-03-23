import numpy as np
import cv2
from cv2 import dnn
import pylab
import matplotlib.pyplot as plt
import time


#pre-trained된 모델 경로
model_path = 'model\\'

if __name__ == "__main__":

    #계산하고자 하는 이미지
    img = r'image\student1.jpg'

    img_ori = cv2.imread(img)
    plt.figure(1)
    plt.imshow(img_ori)
    plt.axis('off')
    pylab.show()


    #RGB값 일부를 제외시켜 이미지 처리를 용이하게 함
    blob = dnn.blobFromImage(img_ori, 1, (1024, 768), (0, 0, 0), True)

    current = time.localtime()

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

    print("계산된 군중 수: ", int(crowd_count))

    plt.figure(1)
    plt.imshow(density[0, 0, :, :])
    plt.axis('off')
    pylab.show()
