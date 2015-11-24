#!/usr/bin/python
__author__ = 'oakdragon'

import sys
from scapy.all import sr1, IP, ICMP
import time
import os, subprocess


def print_dir(pdir):
    print(dir(pdir))


def current_time():
    dt = time.ctime()
    return dt


def get_user_name():
    import getpass
    user = getpass.getuser()
    return user


def get_user_uid():
    import os
    uid = os.getuid()
    return uid


def get_user_group():
    import os
    ugroup = os.getgroups()
    return ugroup


# print(subprocess.call("ls", shell=True))

# import db_Connect as db



# db.db.db_print('self',db.db.conn)


def get_net_connect_status():
    import os, subprocess
    nethw = []
    netConnection = []
    command = "cat /sys/class/net/"
    command1 = "/carrier"
    n = os.listdir('/sys/class/net/')
    for i in n:
        nethw = n
    wlan = os.popen(command + nethw[0] + command1).read()
    lan = os.popen(command + nethw[1] + command1).read()

    if wlan >= 0:
        print(wlan)
    else:
        print(wlan)

    if lan >= 0:
        print("eth0 is Up")
    else:
        print("eth0 is Down")


def net_Connect():
    import os, netifaces

    ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    ip2 = netifaces.AF_FILE
    print(ip2)


""" This function work only linux and
    use the notify-send to seed the message
"""


def sendMessage(message):

    import subprocess
    subprocess.Popen(['notify-send', message])
    return






"""

import sys, socket, subprocess as sub
# usage __name__ .py 192.168.1.1 80 90
if 4 != len(sys.argv):
    print("Usage: {} <ip-address> <start-port> <end-port>".format(sys.argv[0]))
    exit()

startPort = 0
endPort = 0


# this is for testing the port number is entered correctly

try:

    startPort = int(sys.argv[2])
    endPort = int(sys.argv[3])
except:
    print("There is error in the Port Number")
    exit()

# lets begin

while startPort <= endPort:
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sys.argv[1]).startPort)

        print("Port {} is Opened".format(startPort))
        startPort = startPort + 1
        sock.close()
    except:
            print("Port {} is Closed".format((startPort)))
            startPort = startPort +1

"""


def ifconfig_iface():
    from subprocess import check_output

    ifconfig = check_output(['ifconfig', 'eth0'])
    ifconfig.split()
    iface =(ifconfig.split()[0])
    return iface

def ifconfig_IP():
    # this is for IPV4 not IPV6
    from subprocess import check_output
    # ipv6 is [11]
    ifconfig = check_output(['ifconfig', 'eth0'])
    ifconfig.split()
    ip = (ifconfig.split()[6][5:])
    return ip

def ifconfig_Mac():
    from subprocess import check_output
    # going to get hardware Mac address
    ifconfig = check_output(['ifconfig', 'eth0'])
    ifconfig.split()
    mac = (ifconfig.split()[4])
    return mac

def ifconfig_Bcast():
    from subprocess import check_output

    ifconfig = check_output(['ifconfig', 'eth0'])
    ifconfig.split()
    bcast = (ifconfig.split()[7][6:])
    return bcast


def ifconfig_subnet():
    from subprocess import check_output

    ifconfig = check_output(['ifconfig', 'eth0'])
    ifconfig.split()
    subnet = (ifconfig.split()[8][5:])
    return  subnet

def ifconfig_IPV6():
    from subprocess import check_output
    ifconfig = check_output(['ifconfig', 'eth0'])
    ifconfig.split()
    ipv6 = (ifconfig.split()[11])
    return ipv6



