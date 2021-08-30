#!/usr/bin/env python3
from PyP100 import PyP100
import time

ip_address    = TODO
email_address = TODO
password      = TODO

def main():
    p100 = PyP100.P100(ip_address, email_address, password)

    # Creates the cookies required for further methods 
    p100.handshake()
    # Sends credentials to the plug and creates AES Key and IV for further methods
    p100.login()

    #p100.turnOn()
    #time.sleep(5)
    p100.turnOff()
    print(p100.getDeviceInfo())

if __name__ == "__main__":
    main()
