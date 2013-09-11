#!/usr/bin/env python2.7

import sys
import io

# utils
from utils import bind9

def main(argv):

    bind9.install()
    
    answer = False
    print "Run apt-get update? (y/N):"
    ans = sys.stdin.readline()
    if ans.startswith("y"):
        io.system("apt-get update")

    print "Run apt-get upgrade? (y/N):"
    ans = sys.stdin.readline()
    if ans.startswith("y"):
        io.system("apt-get upgrade -y")
    
    print "Install and configure bind9? (y/N):"
    ans = sys.stdin.readline()
    if ans.startswith("y"):
        bind9.install()

if __name__ == '__main__':
    main(sys.argv)