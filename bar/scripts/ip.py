#!/usr/bin/env python3

import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('', 0))
    
    print(s.getsockname()[0])
except:
    print("Disconnected")
