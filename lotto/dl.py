#!/usr/bin/env python2.7

from core import *
from analyse import *

# duzy lotek function
def dl():

  print "--------  LOTTO   ------"
  data_dict = import_data("dl_razem.txt")
  num_dict, last_lottery_dict = generate_num_tab(data_dict, 49)
  sorted_num_dict = sort_by_freq(num_dict)
  sorted_last_lottery_dict = sort_by_last_occurence(last_lottery_dict)
  print "six low  frequency numbers:",
  print sorted(sorted_num_dict[:6])
  print "six high frequency numbers:",
  print sorted(sorted_num_dict[-6:])
  print "last_lottery low frequency:", 
  print sorted(sorted_last_lottery_dict[-6:])
  
  for i in xrange(3):
    #print "low frequency x last_lottery:",
    print sorted(generate_numbers(data_dict, list1=sorted_num_dict[:6], list2=sorted_last_lottery_dict[-6:], list3=[]))
  
  for i in xrange(3):
    #print "high frequency x last_lottery:",
    print sorted(generate_numbers(data_dict, list1=sorted_num_dict[-6:], list2=sorted_last_lottery_dict[-6:], list3=[]))
  
  for i in xrange(3):
    #print "low frequency x last_lottery x high_frequency:",
    print sorted(generate_numbers(data_dict, list1=sorted_num_dict[:6], list2=sorted_last_lottery_dict[-6:], list3=sorted_num_dict[-6:]))
