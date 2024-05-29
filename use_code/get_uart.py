import serial.tools.list_ports
import time

def getUart():
    try:
        while True:
            time.sleep(0.2)  # 减少检查频率，减轻CPU负担
            ports_list = list(serial.tools.list_ports.comports())
            if ports_list:  # 检查列表是否非空
                for comport in ports_list:
                    if comport.device == 'COM11':  # 直接访问属性
                        print("串口COM11已连接。")
                        return True
                print("串口号错误。")
            else:
                print("无串口设备。")
    except:
        return False

