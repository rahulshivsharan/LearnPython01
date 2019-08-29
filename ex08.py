def func():
    map = {
		   11 : "Viktor Lutof",
       8 : "Xander Charlton",
		   3 : "Abott Hamilton"
	}

    # defining inner function which returns key from dictionary
    def fn(keyAndVal):
        return keyAndVal[1]

    # passing  the above function to the key attribute for 'sorted' function
    # which returns list of tuple's,
    # the list is sorted as per value 
    sortedList = sorted(map.items(), key = fn)
	
    print(sortedList);

func()
