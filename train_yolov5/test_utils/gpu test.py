import cv2
import torch
import time
from torchvision import transforms

# Model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='../yolov5/runs/train/exp/weights/last.pt').to(device)

transform = transforms.Compose([
    transforms.ToTensor(),  # 直接使用ToTensor()将图像数据转换为张量
])

# 打开摄像头
cap = cv2.VideoCapture(0)
ptime = 0

while True:
    # 从摄像头读取帧
    ret, frame = cap.read()
    img = frame.copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if not ret:
        break

    # 将OpenCV读取的图像转换为张量并移动到GPU
    img_tensor = transform(frame).unsqueeze(0).to(device)
    results = model(img_tensor)

    # 在帧上绘制检测结果
    for *xyxy, conf, cls in results.xyxy[0]:
        if conf > 0.8:
            label = f'{model.names[int(cls)]} {conf:.2f}'
            cv2.rectangle(img, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 0, 255), 2)
            cv2.putText(img, label, (int(xyxy[0]), int(xyxy[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    # 显示帧
    cv2.imshow('YOLOv5 Real-time Object Detection', img)

    # 按'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()