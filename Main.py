
#-*- coding : utf-8-*-
# coding: utf-8
# coding:unicode_escape


import socket
import time
 

HOST = '0.0.0.0'
PORT = 2000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

def Get_DATA():
    message = [0]
    try:
        client_socket, client_address = server_socket.accept()
   
        message = client_socket.recv(4096)
        #帧头
        if message[0] == 0xA5 and message[1] == 0x5A :
            print("Upload time: " + time.strftime("%Y-%m-%d %H:%M:%S"),flush=True)
            print(f'Client connected from {client_address}',flush=True)

            #软件版本号
            print("    软件版本号: " + str(message[6]),flush=True)
            #数据类型
            print("      数据类型: " + str(message[8]),flush=True)
            #设备ID
            print("        设备ID: " + str(message[9:19]),flush=True)
            #IMEI号
            print("          IMEI: " + str(message[19:34]),flush=True)
            #IMSI号
            print("          IMSI: " + str(message[34:49]),flush=True)
            #熄灭屏幕上传有效位
            print("屏幕上传有效位: " + str(message[49]),flush=True)
            #电池电量
            print("      电池电量: " + str(message[50] * 3 / 100.0),flush=True)
            #信号强度
            print("      信号强度: " + str(message[51]),flush=True)
            #报警状态
            fault = "无"
            if message[52] == 0x01 :
                fault = "IIC故障"
            elif message[52] == 0x02 :
                fault = "压力异常"
            elif message[52] == 0x03 :
                fault = "IIC故障、压力异常"
            print("      报警状态: " + str(fault),flush=True)
            #传感器类型
            fault = "未知"
            if message[53] == 1 :
                fault = "2860"
            elif message[53] == 2 :
                fault = "2302"
            elif message[53] == 3 :
                fault = "1203"
            elif message[53] == 4 :
                fault = "1400"
            print("    传感器类型: " + str(fault),flush=True)
            #量程上下限
            print("      量程上限: " + str((message[56] << 8 | message[57]) / 100.0),flush=True)
            print("      量程下限: " + str((message[54] << 8 | message[55]) / 100.0),flush=True)
            #UTC
            print("           UTC: " + str(message[58] << 24 | message[59] << 16 | message[60] << 8 | message[61]),flush=True)
            #数据记录间隔
            print("  数据记录间隔: " + str(message[62] << 8 | message[63]) + "s",flush=True)
            #数据记录总数
            print("  数据记录总数: " + str(message[64] << 8 | message[65]) + "次",flush=True)
    except:
        print("!数据不完整或非协议内容!",flush=True)
        print("字符串数据: " + str(message),flush=True)
    #    response = 'Hello from server!'
    #    client_socket.send(response.encode('utf-8'))
    #原始数据
    print("      原始数据: " + message.hex(' ') + '\n',flush=True)
    client_socket.close()


print(f'Server is listening at {HOST}:{PORT}',flush=True)


if __name__ == '__main__':
    while True :
        Get_DATA()


 
