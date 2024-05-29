import cv2

def stratPress(cap):
    while True:
        _, img = cap.read()
        cv2.rectangle(img, (0, 100), (640, 250), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Camera Text Pass", (100, 160), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.putText(img, "Press S to start ", (100, 240), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("test", img)
        #按下s跳出循环开始运行
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    cv2.destroyWindow("test")
    print("Start")
