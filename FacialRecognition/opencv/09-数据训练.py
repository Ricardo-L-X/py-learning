import os
import cv2 as cv
from PIL import Image
import numpy as np


def getImageAndLabels(path):
    # 储存人脸数据
    facesSamples = []
    # 储存名字
    ids = []
    # 储存图片信息
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 加载分类器
    face_detector = cv.CascadeClassifier(
        '/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    # 遍历图片
    for imagePath in imagePaths:
        # 打开图片，灰度化 PIL
        '''
            PIL有九种不同模式：1(黑白）,L（灰度）,P,RGB,RGBA,CMYK,YCbCr,I,F
        '''
        PIL_img = Image.open(imagePath).convert('L')
        # 将图像转化为数组，黑白的深浅
        '''
            转换成灰度后，就可以用0-255数字来表示，这样就相当于向量化，存到 img_numpy 数组中，表示的就是一整张图片
        '''
        img_numpy = np.array(PIL_img, 'uint8')
        # 获取图片人脸特征
        '''
            把一整张图片的人脸的那一部分框起来
        '''
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])  # 看命名，如果是1-jjy就用-分隔
        # 预防无面容的照片
        '''
            这就是把人的id和脸部特征对应起来，同一个下标下的两个数组 ids 和 facesSamples 元素就是对应起来的
        '''
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])
        # 打印脸部特征和id
        print("id: ", id)
        print("fs: ", facesSamples)
    return facesSamples, ids


if __name__ == '__main__':
    # 图片路径
    path = './data/exist/'
    # 读取图像数组和id标签数组和签名
    faces, ids = getImageAndLabels(path)
    # 加载识别器
    recognizer = cv.face.LBPHFaceRecognizer_create()
    # 训练，将身份信息和图片整合
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write('trainer/trainer.yml')
