#Internet Speedtester / Made by Kevin Sugar @09/24/2020

import os
import re
import subprocess
import time
import socket
from datetime import datetime
import plotext.plot as plx

def RunSpeedtest():
    global ping
    global download
    global upload
    global test_time

    response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    test_time = datetime.now()
    test_time = test_time.strftime('%H:%M')
    ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
    download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
    upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

    ping = ping[0].replace(',', '.')
    download = download[0].replace(',', '.')
    upload = upload[0].replace(',', '.')

def print_results():
    os.system('clear')
    print('----------------------')
    print('| DL:{:^16}|'.format(download + "MBit/s"))
    print('| UL:{:^16}|'.format(upload + "MBit/s"))
    print('| LT:{:^16}|'.format(ping + "ms"))
    print('----------------------')
    print('Time of test: ' + test_time)

def socket_exception():
    print('NO INTERNET CONNECTION!')
    print('NO INTERNET CONNECTION!')
    print('NO INTERNET CONNECTION!')
    print('NO INTERNET CONNECTION!')
    print('NO INTERNET CONNECTION!')
    time.sleep(5)


while True:

    try:
        RunSpeedtest()
        print_results()
        time.sleep(300)

    except socket.error as e:
        socket_exception()
        pass
