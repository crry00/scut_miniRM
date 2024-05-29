import time
from Yologet import Yologet
import cv2
# Model

# yolo=Yologet('yolov5/runs/train/exp/weights/last.pt')

yolo=Yologet('../best.pt')

# 打开摄像头
cap = cv2.VideoCapture(0)
ptime=0
while True:
    # 从摄像头读取帧
    ret, frame = cap.read()
    img=frame.copy()

    if not ret:
        break

    # 使用YOLOv5进行目标检测
    location=yolo.getlocation(frame)
    print(location)

    if location is not False:
        for i,[x,y] in enumerate(location):
            cv2.putText(img, f"{i}", (x, y), cv2.FONT_HERSHEY_PLAIN,
                        2, (0, 255, 0), 1)

    # 在帧上绘制检测结果
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    # 显示帧
    cv2.imshow('YOLOv5 Real-time Object Detection', img)

    # 按'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()