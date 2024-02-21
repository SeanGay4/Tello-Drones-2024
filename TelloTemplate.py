# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

print("\n Sean Gay + Team Member: Cade Smith " )
print("Program Name: Program FLight ")
print("Date: 2.6.2024 ")
print("DEC7")
print("\nFirst & Last Names")
print("Program Name: ")
print("Date: ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")
        
        sendmsg('command', 0)
        sendmsg('battery?')
        sendmsg('takeoff')

        # first hoop: seans computer


        sendmsg("up 20", 8)
        sendmsg("forward 200", 8)

        # second hoop: cades computer
        sendmsg("go 205 0 40 70", 10)


        # curve into thrird hoop: seans computer

        sendmsg('curve 125 125 0 0 250 0 50', 15)
        sendmsg('cw 180',8)
        sendmsg('forward 40',8)

        # descend and finish: cades computer
        sendmsg('go 225 0 -75 50', 10)
        sendmsg('forward 30')

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
