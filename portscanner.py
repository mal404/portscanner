#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #translate host name into IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax:python3 portscanner.py <ip>")

#Add pretty banner
print("-" * 60)
print("Scanning the target "+target)
print("Time started: "+str(datetime.now()))

try:
    for port in range (20,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns indicator
    
        if result == 0:
            print("Port {} is open".format(port))
            s.close()
            
except KeyboardInterrupt:
    print("\nExitingProgram.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not resolved")
    sys.exit()

except socket.error:
    print("Could connect to server")
    sys.exit()

