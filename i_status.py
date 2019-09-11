import colorsys
import signal
import time
import socket

# Pimironi blinkt lib
from blinkt import set_brightness, set_all, show

def sigGandler(signal, frame):
  sys.exit(0)
  
signal.signal(signal.SIGINT, signal_handler)

# site to ping for alive
hostname = 'google.com'

# LED brightness 1.0 - 0.1 (highest - lowest)
set_brightness(0.1) 

while True:
    #Test socket and DNS.
    try:
        socket.gethostbyname(hostname)
        dns = True
    except socket.error as err:
        dns = False

    x = 0
    while x < 50:
        if dns:
            # Connection alive, network online.
            set_all(80, 140, 80)
            print('Online!')
        else:
            # Connection down, network offline.
            set_all(0, 255, 0)
            print('Offline!')
        show()
        x += 1
        # 90 second sleep for rate limits (can be adjusted as required)
        time.sleep(90)
