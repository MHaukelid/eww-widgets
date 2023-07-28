#!/usr/bin/env python3

from socket import gethostbyname, gethostname

try:
    print(gethostbyname(gethostname()))
except:
    print("Disconnected")
