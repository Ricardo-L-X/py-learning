# 导入模块
import cv2 as cv

cap = cv.VideoCapture(0)

flag = 1
num = 1

while(cap.isOpened()):
    # 得到每帧图像
    ret_flag, Vshow = cap.read()
    # 显示图像
    cv.imshow("Capture_test", Vshow)
    # 按键判断
    while True:
        if ord("s") == cv.waitKey(1):
            cv.imwrite("/Users/ricardo/Desktop/PythonProject/FacialRecognition/opencv/data/save/"+str(num)+"-name"+".jpg", Vshow)  # name 是人的名字
            print("success to save"+str(num)+".jpg")
            print("------------------------------------")
            num+=1
        elif cv.waitKey(1) == ord(" "):   # 退出
            break


cap.release()

cv.destroyAllWindows()