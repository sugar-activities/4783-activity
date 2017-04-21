#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import platform

secs = 10

def show_message(message):
    # For python2 and python3
    try:
        print message
    except:
        print(message)

show_message("Sorry, this is the x86 version, this can't be runned on a %s computer" % platform.architecture()[0])
show_message("Closing activity")

while True:
    show_message(secs)

    secs -= 1
    if (secs < 1):
        break

    time.sleep(1)


sys.exit(0)
