import cv2 as cv

# 读取图片
img = cv.imread('1.jpg')

# 显示图片
cv.imshow('read_img', img)

# 等待
cv.waitKey(10000) # 图片显示10000ms

# 释放内存
cv.destroyAllWindows()