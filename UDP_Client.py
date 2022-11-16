from socket import *


# 确定服务器的地址
ADDR = ("127.0.0.1", 8888)

# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 是否需要绑定？    客户端默认由操作系统分配端口     绑定了就是固定了客户端的地址

# 循环发送消息
while True:
    # 接收信息
    msg = input(">>> ")

    # 发送给服务器
    udp_socket.sendto(msg.encode(), ADDR)

    #接收服务器返回的消息
    data, addr = udp_socket.recvfrom(1024)
    print("Recv:", data.decode(), addr)
    #终止客户端循环
    if msg == "bye":
        break


# 关闭套接字
udp_socket.close()