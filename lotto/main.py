#!/usr/bin/env python2.7

import sys
import os
import random
import dl
import mini

from core import *

# main function
def main(argv):
  logo()
  if(len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] == "help")):
    help()
  
  elif(len(sys.argv) == 1):
    dl.dl()
    mini.mini()
    # generate for both
    
  elif(sys.argv[1] == 'lotto'):
    dl.dl()
  
  elif(sys.argv[1] == 'mini'):
    mini.mini()
  
if __name__ == "__main__":
  main(sys.argv)