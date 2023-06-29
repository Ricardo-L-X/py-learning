import cv2 as cv

# 建立检测函数
def face_detect_demo(img):
    # 先把图片灰度化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 调取分类器
    face_detect = cv.CascadeClassifier('/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(image=gray,
                                        scaleFactor=1.075, # 这个值需要不断调整，如果没有调到适合值，可能会误触 1.07
                                        minNeighbors=5,
                                        flags=0,
                                        minSize=(70, 70), # 人脸最小，100*100的框中不可能有人脸 可不填
                                        maxSize=(100, 100)) # 人脸最大，1000*1000的框外不可能有人脸 可不填
    '''
        detectMultiScale函数的几个参数是 灰度图像 每次缩放倍数 每次检测5次这里都有人脸后才算数 不管 最小范围 最大范围
    '''
    for x,y,w,h in face:
        # 在原图上画矩形，把人脸框出来
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

# 读取图片
img = cv.imread('2.jpg')

# 检测函数
face_detect_demo(img)

# 等待
while True:
    if ord('q') == cv.waitKey(0):  # 按下q键，退出图片显示
        break

# 释放内存
cv.destroyAllWindows()