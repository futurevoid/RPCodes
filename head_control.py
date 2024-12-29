from socket import *

UDPCliSock = socket(AF_INET,SOCK_DGRAM)
def headangle(angle,ADDR):
    angle_hex = str(hex(angle))
    if angle < 16:
        data = str("{\"cmd\":\"servo\", \"type\":\"write\",\"time\":35,\"angle\":\"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" + str(0) + angle_hex[-1] + "\"}")
        #UDPCliSock.sendto(data,ADDR)
        print(data)
    else:    
        data = str("{\"cmd\":\"servo\", \"type\":\"write\",\"time\":35,\"angle\":\"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF" + angle_hex[2] + angle_hex[3] + "\"}")
        #UDPCliSock.sendto(data + angle_hex[2] + angle_hex[3] + end,ADDR)
        print(data)


if __name__ =='__main__':
    print("UDP Communication Test Start")
    HOST = "127.0.0.1"
    PORT = "20001"
    ADDR = (HOST,PORT)
    headangle(15,ADDR)
    print("UDP Communication Test Finished")
    