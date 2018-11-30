#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys

from ICMP.IcmpApp import IcmpSender, IcmpReceiver


def show_usage ():
    print """
      USAGE:
        icmp.py recv <destination file>
        icmp.py send <file to transfer> <remote address>
    """
    exit()


if __name__ == '__main__':
    try:
        action = sys.argv[1]
        filename = sys.argv[2]
    except IndexError:
        show_usage()

    if action == 'send': 
        try:    dst_addr = sys.argv[3]
        except: show_usage()

        with IcmpSender(filename) as sender:
            sender.send(dst_addr)

    elif action == 'recv': 
        with IcmpReceiver(filename) as receiver:
            receiver.receive()


