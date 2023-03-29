#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import re


ips = set()
interface = '0.0.0.0'
MCAST_PORT = '组播端口号'
MCAST_ADDR = '239.255.255.250'
message = '发送内容'
# udp组播实现设备发现
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.settimeout(1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((interface, MCAST_PORT))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_ADDR) + socket.inet_aton(interface))
# 发送两次消息，有时一次搜索不完全
sock.sendto(message, (MCAST_ADDR, MCAST_PORT))
sock.sendto(message, (MCAST_ADDR, MCAST_PORT))
while True:
    try:
        data, addr = sock.recvfrom(2048)
    # 通过超时来退出循环
    except socket.timeout:
        break
    except:
        pass

    try:
        ipv4 = re.search(re.compile(r"<IPAddr>(.*?)</IPAddr>", re.S), str(data))[1]
    except:
        pass
    else:
        ips.add(ipv4)

if ips:
    ips = list(ips)
    for i in range(len(ips)):
        print(ips[i])
        
print('设备数：', len(ips))