# -*- coding: utf-8 -*-

import sys
import pwd
import time
import readline
import reqs

def _print(msg):
    line_buffer = readline.get_line_buffer()
    # Clearing prompt
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")
    sys.stdout.write(str(msg))
    # Restoring prompt
    sys.stdout.write("\n%s" % reqs._current_prompt)
    if line_buffer:
        sys.stdout.write(" %s" % line_buffer)
    sys.stdout.flush()

def get_username(auid,log_list,row):
    try:
        username = pwd.getpwuid(int(log_list[row]['auid']))[0]
    except KeyError:
        username = ""
    return username

def format_date(s):
    return time.strftime("%d/%b/%Y %H:%M:%S", time.localtime(float(s)))
