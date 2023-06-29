import os
import cv2 as cv
import urllib
import urllib.request

# 加载训练数据文件
recognizer = cv.face.LBPHFaceRecognizer_create()
# 加载数据
recognizer.read('./trainer/trainer.yml')

# 名称
names=['jjy']
# 警报全局变量
warningtime = 0
# md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode('utf8'))
    return m.hexdigest()   # 就是对密码进行一个加密
# 短信反馈
statusStr = {
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持，请确认支持url或者fsocket，联系客服解决',
    '30':'密码错误',
    '40':'账号不存在',
    '41':'余额不足',
    '42':'账户已过期',
    '43':'IP地址限制',
    '50':'内容有敏感词'
}
# 报警模块
def warning():
    smsapi = "http://api.smsbao.com/"
    # 短信平台账号
    user = '17786661838'
    # 短信平台密码
    password = md5('123456')
    # 要发送信息
    content = '【报警】\n原因：xxx\n地点：xxx\n时间：xxx'
    # 要发送短信的手机号码
    phone = '17786661838'

    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])

# 准备识别的图片
def face_detect_demo(img):
    # 灰度化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 调取分类器
    face_detector = cv.CascadeClassifier('/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    # 识别出正确范围的人脸
    face = face_detector.detectMultiScale(
        image = gray,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=0,
    )
    # 对于识别出的人脸，给人脸画框框
    for x,y,w,h in face:
        # 画方框
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0,0,255), thickness=2)
        # 画圆框
        cv.circle(img, center=(x+w//2, y+h//2), radius=w//2, color=(0, 255, 0), thickness=2)
        # 人脸识别
        ids, confidences = recognizer.predict(gray[y:y+h, x:x+w])
        print('标签id：', ids, '置信评分：', confidences)
        # 判断
        if confidences > 80:  # 如果置信评分超过了80这个界限，则爸警报变量+1
            global warningtime
            warningtime += 1
            if warningtime > 100:  # 一旦警报变量超过了100，则认定为陌生人，发出警报
                warning()
                warningtime = 0
            cv.putText(img, 'unknow', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1)
        else:
            cv.putText(img, str(names[ids-1]), (x+10,y-10),cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1)
    cv.imshow('result:', img)

if __name__ == '__main__':
    # 读取图片
    # img = cv.imread('data/exist/1.jjy.jpg')
    img = cv.imread('./data/exist/1.jjy.jpg')
    # 进行检测
    face_detect_demo(img)
    # 等待
    while True:
        if ord('q') == cv.waitKey(0):
            break
    # 释放内存
    cv.destroyAllWindows()

