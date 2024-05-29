import cv2

image=cv2.VideoCapture("output5_14_2.mp4")

num=0 #照片命名从哪个数开始
save_step=0
while True:
    ret,frame=image.read()
    if not ret:
        print("false")
        break
    save_step+=1
    if save_step==15:#多少帧裁剪一张图片
        cv2.imwrite("./GXS2_0/"+str(num)+".jpg",frame)
        num+=1
        save_step=0
    cv2.imshow("img",frame)
    cv2.waitKey(1)