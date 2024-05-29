import cv2
import torch
import time
# Model
model = torch.hub.load('ultralytics/yolov5',"custom", path='../last.pt')
# 打开摄像头
cap = cv2.VideoCapture(0)
ptime=0
while True:
    # 从摄像头读取帧
    ret, frame = cap.read()
    img=frame.copy()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    if not ret:
        break

    # 使用YOLOv5进行目标检测
    results = model(frame)
    print(results.xyxy[0])
    # 在帧上绘制检测结果
    for *xyxy, conf, cls in results.xyxy[0]:
        if conf>0.75:
            label = f'{model.model.names[int(cls)]} {conf:.2f}'
            cv2.rectangle(img, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 0, 255), 2)
            # print(int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3]))
            cv2.putText(img, label, (int(xyxy[0]), int(xyxy[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, f"FPS:{int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN,
                2, (0, 255, 0), 2)

    # 显示帧
    cv2.imshow('YOLOv5 Real-time Object Detection', img)

    # 按'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()