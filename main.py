#!/usr/bin/python
__author__ = 'oakdragon'

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
    return  uid


def get_user_group():
    import os
    ugroup = os.getgroups()
    return  ugroup


print(subprocess.call("ls", shell=True))