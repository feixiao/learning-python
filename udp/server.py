#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from sys import argv

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(argv)

if len(argv) < 2:
    print("no port...")
    exit(-1)

port = int(argv[1])
s.bind(("0.0.0.0", port))

print("UDP bound on port ", port)

while True:
  try:
      data, addr = s.recvfrom(1024)
      print("Receive from %s:%s" % addr)
      s.sendto(b"Hello %s!\n" % data, addr)
  except KeyboardInterrupt:
    break
