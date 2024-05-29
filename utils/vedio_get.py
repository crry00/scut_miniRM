import cv2

# 定义摄像头编号
camera_index = 0

# 创建VideoCapture对象
cap = cv2.VideoCapture(camera_index)
width=640
height=480
cap.set(3,width)
cap.set(4,height)
cap.set(cv2.CAP_PROP_EXPOSURE,-6)#设置曝光
cap.set(cv2.CAP_PROP_CONTRAST, 50)

# 检查是否成功打开了摄像头
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 定义视频编码方式、帧率、分辨率等参数
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4编码器
fps = 20.0
frame_size = (640, 480)  # 分辨率可以根据需要调整

# 创建VideoWriter对象，传入文件名、编码方式、帧率和分辨率
out = cv2.VideoWriter('output5_14_3.mp4', fourcc, fps, frame_size, isColor=True)

while True:
    # 读取一帧图像
    ret, frame = cap.read()

    # 检查是否成功读取了图像
    if not ret:
        print("无法读取摄像头图像")
        break

        # 对图像进行处理（可选）
    # ...

    # 显示图像
    cv2.imshow('Camera Feed', frame)

    # 将图像写入视频文件
    out.write(frame)

    # 等待按键，如果是'q'则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()