import sys
import time

def func():
    date_string = sys.argv[1] # grab date string
    date_object = time.strptime(date_string,"%Y%m%d") # parse date string to date object
    date_string = time.strftime("%d-%b-%Y",date_object)	 # formate date Object ot date string of other pattern
    print(date_string)

func()
