

import cv2
from get_uart import getUart
from cap_init import capInit
from start_press import stratPress
from yolo_get import Yologet
#初始化yolo
yolo=Yologet()

#检测串口
if getUart() is False:
    print("串口错误")

flag=False
from set_angel import *
#初始化舵机和摄像头
sendbyte(74, 100, 1)
cap = capInit()

while True:
    try:
        from class_jiguang import jiguang
        Jiguang=jiguang()
        # 设置正常曝光
        cap.set(cv2.CAP_PROP_EXPOSURE, -4)
        stratPress(cap)

        #######################################2.获得对应坐标########################################
        Location=None
        while True:
            _,img=cap.read()
            #获取坐标
            Location=yolo.getlocation(img)
            if Location is not None:
                break
            cv2.imshow("img",img)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                flag=True
                break
        if flag:
                continue
        print(Location)
        print("获得完毕")
        #######################################3.获得激光位置及移动舵机########################################
        # 相机设置曝光和对比度，降低曝光
        cap.set(cv2.CAP_PROP_EXPOSURE, -8)
        cap.set(cv2.CAP_PROP_CONTRAST, 200)
        plight=[]
        count=0
        while True:
            _,img=cap.read()
            light=Jiguang.getjiguang(img)#获得激光位置
            point=Location[Jiguang.count]
            cv2.circle(img,point,3,(255,0,255),cv2.FILLED)
            if count==10:
                count=0
                print(light,point)
                Jiguang.duoji(light,plight,point)#根据位置移动
            plight=light
            cv2.imshow("img",img)
            count+=1
            if cv2.waitKey(1) & 0xFF == ord('r'):
                flag = True
                break
        if flag:
            continue
    except:
        print("出错")
        sendbyte(74, 100, 1)


