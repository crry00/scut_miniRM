import serial
import time
#打开串口
ser=serial.Serial('com11',9600,timeout=1)

def sendbyte(xangle,yangle,Time):
    if 0<=xangle<=180and 0<=yangle<=180:
        myinput=bytes([0xFF,xangle,yangle,0xFE])
        time.sleep(Time)
        ser.write(myinput)#写数据

