import time
import socket
import urllib.request
from datetime import datetime
import os

last_downtime = "No Downtime yet!"

while True:


    try:
        os.system("clear")
        urllib.request.urlopen("https://hc-ping.com/84e8f0f6-b54e-4cf5-b6bb-e5be6245a5a6", timeout=10)
        print("Ping Successful at " + str(datetime.now()))
        print("Last downtime was at: " + last_downtime)
        print("Next Ping in 20s")
        time.sleep(20)

    except socket.error as e:
        # Log ping failure here...
        print("Ping failed: %s" % e)
        last_downtime = str(datetime.now())
        print("")
        print("INTERNET IS DOWN!!!")
        print("INTERNET IS DOWN!!!")
        print("INTERNET IS DOWN!!!")
        print("INTERNET IS DOWN!!!")
        time.sleep(1)
