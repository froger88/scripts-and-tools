#!/usr/bin/env python2.7

import sys
import os
import random

from analyse import *

# import data from file
def import_data(fname):
  '''
  import data from file
  return data_dict {1: [1,2,3,4,5] }
  '''
  data_dict = {}
  f = file(fname)
  data = f.readlines()
  
  data_dict = {}
  for entry in data:
    en = entry.split()
    id = int(float(en[0]))
    numbers = en[2]
    numbers_list = en[2].split(',')
    numbers_list_int = []
    for entry in numbers_list:
        numbers_list_int.append(int(entry))
    numbers_list = numbers_list_int
    
    data_dict[id] = numbers_list 
  
  return data_dict


# generate clean num_tab
def generate_num_tab(data_dict, size):
  ### num_dict - contain frequency dict, like: {1: 3, 2:0, 3:17}
  num_dict = {}
  ### last_lottery_dict - contain info in which (last last_lottery) occurs
  last_lottery_dict = {}
  for i in xrange(size):
    num_dict[i+1] = 0
    last_lottery_dict[i+1] = 0

  # fill num_dict with frequency data
  # and last_lottery_dict with last_lottery info

  for entry in data_dict:
   for i in data_dict[entry]:
     num_dict[i] += 1
     if entry > num_dict[i]:
       last_lottery_dict[i] = entry

  return num_dict, last_lottery_dict



# print logo
def logo():
  logo = '''
  #######################################
  #####  LOTTO GENERATOR BY FROGER  #####
  #############  v. 1.1.0  ##############
  
  '''
  print logo


# numbers generator
def generate_numbers(data_dict, list1=[], list2=[], list3=[]):
  main_list = []
  for en in list1,list2,list3:
    if en not in main_list:
      main_list += en

  #generate 1000'000 numbers: 18!/(6!(18-9)!), but save lowest similarity of them:
  
  #out_sim_list = [([list of numbers], similarity), ...]

  for i in xrange(1000000):
    j = 0
    out = []
    while j < 6:
      num = random.choice(main_list)
      if num not in out:
        out.append(num)
        j += 1
    
    # check similarity
    for entry in data_dict:
      x = similarity(data_dict[entry], out)
    if x == 2:
      return out
    


def help():
  print "usage:"
  print " $./main.py - to generate numbers for 'duzy lotek' and 'mini' lottery"
  print " $./main.py help - to show this screen"
  print " $./main.py lotto - to generate numbers for 'duzy lotek' lottery"
  print " $./main.py mini - to generate numbers for 'mini' lottery"