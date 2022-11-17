from socket import socket

# 声明服务器IP, 端口
ADDR = ("0.0.0.0", 8888)

# 创建 udp 套接字
# AF_INET 为固定参数   AF_INET代表IPv4，
# SOCK_DGRAM 表示使用的是udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 调用函数， 绑定端口
udp_socket.bind(ADDR)

# 循环接收消息
while True:
    # recvfrom 被动接收链接
    # 接收消息   1024为一次能接受的最大字节数
    msg, addr = udp_socket.recvfrom(1024)
    print("Recv:", addr, msg.decode())

    # 回应消息
    udp_socket.sendto("收到！".encode(), addr)

    # 约定断开通信的暗号
    if msg == b"bye":
        break

udp_socket.close()
