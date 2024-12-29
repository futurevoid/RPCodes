import sys
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST

def sendmsg(ip,buf):
    PORT = 20005
    ADDR = (ip,PORT)
    UDPClientSock = socket(AF_INET,SOCK_DGRAM)
    UDPClientSock.setsockopt(SOL_SOCKET,SO_BROADCAST)
    UDPClientSock.sendto(buf,ADDR)
    UDPClientSock.close()


def action_func(Name, repeat):
    send_string = "{\"cmd\":\"action\",\"type\":\"start\",\"para\":\"{\"name\":\""+ Name +"\",\"repeat\":"+ str(repeat) + "}}"
    print(send_string)
    sendmsg("255.255.255.255",send_string)


if __name__ == "__main__":
    default_port = 20006
    if len(sys.argv) == 2:
        action_name = sys.argv[1]
        action_func(action_name,1)
    elif len(sys.argv) == 3:
        action_name = sys.argv[1]
        repeat = int(sys.argv[2])
        action_func(action_name,repeat)
    else:
        print("Syntax: python sc.py action_name [repeat]") 