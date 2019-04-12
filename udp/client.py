#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from sys import argv
import time

if len(argv) < 3:
    print("input error")
    print(argv)
    exit(-1)

address = argv[1]
port = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (address, port)


while True:
  try:
      str = "tester"
      s.sendto(bytes(str, encoding="utf8"), addr)
      response, addr = s.recvfrom(1024)
      print("Receive from %s:%s" % addr)
      print(response.decode())
      time.sleep(10)
  except KeyboardInterrupt:
    break
