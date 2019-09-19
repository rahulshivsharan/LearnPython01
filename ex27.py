
def fun01():
    nList = [2,4,3,7]
    print("Original List ",nList) # printing original list
	
    # looping through list 'nList' and multiple each element by 2
    newList = [x*2 for x in nList]
	
    print("Mulitply each element by 2")
    print("Product of 2 ",newList)	

    nList = [12,45,15,67,28,19]
    print("Original List ",nList) # printing original list

    # filtering only even numbers
    newList = [num for num in nList if num%2 == 0]    
    print("Even Number list ",newList)


    # looping through and applying lambda expression
    nList = [23,42,64,18,24,67,23,89]	
    print("Original List ",nList) # printing original list
	
    # filter function 
    def fn(num):
        return (num%3 == 0)
		
    filterFn = filter(fn,nList) # get the filter refenrence 		
    newList = list(filterFn)
    print("Number divisible by three ",newList)    
	
	
fun01()
