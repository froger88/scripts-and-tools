#!/usr/bin/env python2.7

import sys
import os
import random

def similarity(list1, list2):
    '''
       calc similarity between list1 and list2
       0 means there is no the same entries in lists
    '''
    similarity = 0
    for entry in list1:
        if entry in list2:
            similarity +=1

    return similarity

def import_data(fname):
  '''
  import data from file
  return data_dict {1: [1,2,3,4,5,6] }
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


def generate_num_tab(data_dict):
  '''
     generate clean num_tab
  '''
  ### num_dict - contain frequency dict, like: {1: 3, 2:0, 3:17}
  num_dict = {}
  ### last_lottery_dict - contain info in which (last last_lottery) occurs
  last_lottery_dict = {}
  for i in xrange(49):
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

# sort by frequency
def sort_by_freq(num_dict):
  sorted_num_dict = sorted(num_dict, key=num_dict.get)

  min_value = num_dict[sorted_num_dict[0]]
  '''
  print 7x7 tab with frequency of each number
  
  for en in num_dict:
    print "%3d |" % (num_dict[en][0] - min_value),
    if en % 7 == 0:
      print "\n"
  '''
  
  return sorted_num_dict

def sort_by_last_occurence(last_lottery_dict):
  last_lottery_dict_sorted = sorted(last_lottery_dict, key=last_lottery_dict.get)

  min_value = last_lottery_dict[last_lottery_dict_sorted[0]]

  '''
  print 7x7 tab with frequency of each number
  
  i = 1
  for en in last_lottery_dict_sorted:
    print "%3d |" % (last_lottery_dict[en]),
    if i % 7 == 0:
      print "\n"
    i+=1
  '''
  
  
  return last_lottery_dict_sorted


#for en in num_dict:
#  print "%d: %d" % (en, num_dict[en][0])

#print num_dict
#print data_dict

def logo():
  logo = '''
  #######################################
  #####  LOTTO GENERATOR BY FROGER  #####
  #############  v. 1.0.0  ##############
  
  '''
  print logo

def generate_numbers(data_dict, list1=[], list2=[], list3=[]):
  main_list = []
  for en in list1,list2,list3:
    if en not in main_list:
      main_list += en

  #generate 24'504'480 numbers: 18!/(6!(18-9)!), but save lowest similarity of them:
  
  #out_sim_list = [([list of numbers], similarity), ...]

  for i in xrange(24504480):
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


def main():
  logo()
  data_dict = import_data("dl_razem.txt")
  num_dict, last_lottery_dict = generate_num_tab(data_dict)
  sorted_num_dict = sort_by_freq(num_dict)
  sorted_last_lottery_dict = sort_by_last_occurence(last_lottery_dict)
  #print "six low  frequency numbers:",
  print sorted_num_dict[:6]
  #print "six high frequency numbers:",
  print sorted_num_dict[-6:]
  #print "last_lottery low frequency:", 
  print sorted_last_lottery_dict[-6:]
  
  for i in xrange(3):
    #print "low frequency x last_lottery:",
    print generate_numbers(data_dict, list1=sorted_num_dict[:6], list2=sorted_last_lottery_dict[-6:], list3=[])
  
  for i in xrange(3):
    #print "high frequency x last_lottery:",
    print generate_numbers(data_dict, list1=sorted_num_dict[-6:], list2=sorted_last_lottery_dict[-6:], list3=[])
  
  for i in xrange(3):
    #print "low frequency x last_lottery x high_frequency:",
    print generate_numbers(data_dict, list1=sorted_num_dict[:6], list2=sorted_last_lottery_dict[-6:], list3=sorted_num_dict[-6:])
  
  
  #out_list_2 = generate_numbers(data_dict, list1=sorted_num_dict[:6], list2=sorted_last_lottery_dict[-6:], list3=[], cnt=10)
  #out_list_3 = generate_numbers(data_dict, list1=sorted_num_dict[:6], list2=sorted_last_lottery_dict[-6:], list3=[], cnt=10)
  
main()