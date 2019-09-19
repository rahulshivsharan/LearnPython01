
def fun01():
    # intialising dictionary
    tel = {
        2341 : 'jack',
        4356 : 'ron',
        1265 : 'swet' 
    }
    keyList = tel.keys() # extracting keys
    
	# iterating through dictionary 'tel' by using keys
    for k in keyList:
        print("KEY ",k," VALUE ",tel[k])
    
    keyList = sorted(keyList) # sorting keys 
	
    print("--------------")
	
	# iterating dictionary 'tel' using 
    for k in keyList:
        print("KEY ",k," VALUE ",tel[k])
		


fun01()
