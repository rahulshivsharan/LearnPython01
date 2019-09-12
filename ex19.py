
def cubeFun(x):    
    x = (x * x * x)
    return x

def fun01():
    my_list = [5,2,4]
    print(my_list)		
    my_list = [cubeFun(x) for x in my_list] # applying function of cube of numbers for each element in list
    print(my_list)	

fun01()
