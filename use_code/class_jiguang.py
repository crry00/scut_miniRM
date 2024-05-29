import cv2
import numpy as np
from set_angel import *
import time

class jiguang:
    red=None
    anglex=None
    angley=None

    def __init__(self,colorhsv=[160, 80, 30, 179, 255, 255],angleX=100,angleY=74):
        self.red=colorhsv#hsv色域
        self.anglex=angleX#舵机初始化角度
        self.angley=angleY#舵机初始化角度

    def getjiguang(self,img,threshold=1500):
        #通过hsv识别获得激光坐标
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array(self.red[0:3])
        upper = np.array(self.red[3:6])
        mask = cv2.inRange(imghsv, lower, upper)
        kernel = np.ones((5, 5))
        mask=cv2.dilate(mask,kernel,iterations=2)
        # 转换为灰度图
        # 寻找轮廓
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 找到最大面积的轮廓
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if threshold>area> max_area:
                max_area = area
                max_contour = contour
        # 计算最大面积轮廓的中心点
        if max_contour is not None:
            M = cv2.moments(max_contour)
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            cv2.circle(img,(center_x,center_y),3,(0,255,0),cv2.FILLED)
            return [center_x, center_y]
        else:
            return None

    def run(self,light,point):#根据像素差值返回舵机角度
        x=light[0]-point[0]
        y=light[1]-point[1]
        angleX=0
        angleY=0
        #无脑调参
        if x>100or x<-100:
            angleX=int(x/12)
        elif x>60or x<-60:
            angleX=int(x/12)
        elif x>30or x<-30:
            angleX = int(x / 10)
        if y > 100or y<-100:
            angleY = int(y / 12)
        elif y > 60or y<-60:
            angleY = int(y / 12)
        elif y > 30or y<-30:
            angleY = int(y / 10)
        if angleX==0and angleY==0:
            cv2.waitKey(200)
            return True
        self.anglex+=angleX
        self.angley-=angleY
        print(self.anglex,self.angley)
        return False

    count=0#五个图像
    def duoji(self,light,plight,target):
        if light is not None:#如果检测到激光
            ret= self.run(light, target)#移动
            if ret== True:#代表激光已经到达当前目标点，进行下一个目标
                self.count += 1
                time.sleep(1)
                if self.count == 5:
                    print("end")
                    time.sleep(10)
            else:
                # print(y)
                sendbyte(self.angley, self.anglex, 1)
        elif light is None and len(plight)!=0:#如果没检测到激光，则按照最后一次记录的激光点移动，程序有待完善
            ret= self.run(plight, target)
            if ret == True:
                self.count += 1
                if self.count == 5:
                    print("end")
                    time.sleep(10)
            else:
                sendbyte(self.angley, self.anglex, 1)

