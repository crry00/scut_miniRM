import cv2

def capInit():#初始化摄像头
    cap = cv2.VideoCapture(0)
    width = 640
    height = 480
    cap.set(3, width)#宽
    cap.set(4, height)#高
    cap.set(10, 150)#亮度（貌似没卵用）
    cap.set(cv2.CAP_PROP_EXPOSURE, -4)#曝光
    cap.set(cv2.CAP_PROP_CONTRAST, 50)#对比度（貌似没卵用）
    return cap
