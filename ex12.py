import sys
import time

def func():
    date_string = sys.argv[1] #date in string formate
    date_pattern_original = sys.argv[2] # initial date pattern format
    new_date_pattern = sys.argv[3] # convert to this date pattern
    date_object = time.strptime(date_string,date_pattern_original) # get Date object from string
    date_string = time.strftime(new_date_pattern,date_object)	 # convert string from date
    print(date_string)

func()
