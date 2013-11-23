#!/usr/bin/env python2.7

import sys
import os
import random

from core import *

def similarity(list1, list2):
    '''
       calc similarity between list1 and list2
       0 means there is no the same entries in lists
    '''
    similar = 0
    for entry in list1:
        if entry in list2:
            similar +=1

    return similar
  
# sort by frequency
def sort_by_freq(num_dict):
  sorted_num_dict = sorted(num_dict, key=num_dict.get)

  min_value = num_dict[sorted_num_dict[0]]
  
  return sorted_num_dict


# sort by frequency
def sort_by_last_occurence(last_lottery_dict):
  last_lottery_dict_sorted = sorted(last_lottery_dict, key=last_lottery_dict.get)

  min_value = last_lottery_dict[last_lottery_dict_sorted[0]]
  
  return last_lottery_dict_sorted
