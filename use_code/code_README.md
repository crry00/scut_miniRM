### 目录说明
| 文件名 | 用途 |
| - | -|
| cap_init.py| 初始化摄像头|
| class_jiguang.py|激光类|
| get_uart.py |串口|
| main.py| 主程序|
| set_angel.py|控制舵机|
| start_press.py |启动ui界面|
| yolo_get.py |yolo类|

## 代码逻辑与亮点
### cap_init.py
+ 初始化宽高，曝光对比度等
### class_jiguang.py
+ 定义了激光类及其类方法
	+ getjiguang（） 通过hsv识别识别激光坐标
	+ run（）通过像素差✖对应不同权重转换为舵机运动角度
	+ duoji（）舵机运动控制代码，接收run中输出的角度，根据目标和识别的不同情况对应控制
###  get_uart.py
+ getUart（）检测串口是否接通
###  set_angel.py
+ sendbyte（）发送水平和竖直方向运动角度给下位机
###  start_press.py
+ 按下s即可启动
###  yolo_get.py
+ 定义了激光类及其类方法
	+ init构造函数通过pytorch的API加载模型
	+ getresult（） 接收图片，推理
	+ getlocation（）推理，返回需要激光到达的5个坐标点（已排序），具体代码可参考下图
	+ ![getlocation（](/imgs/2024-05-27/7HSz46ckjFzyN00u.png)
###  main.py
(1) 由于通过torch启动yolo模型时间较长，在登场前先初始化摄像头和模型，启动串口检测
(2) 检测到串口后回复舵机,启动ui界面等待启动
(3)启动后先调用yolo获取对应坐标
(4)后调用激光类根据目标和激光坐标移动舵机

> 由于校内赛结束后笔者摆烂，没有对代码进行过多润色，其中有些许混乱处请多多包含，主打一个保留比赛的原汁原味！！！
