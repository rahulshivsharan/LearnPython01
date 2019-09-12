
def addBy10(x):
    x += 10 
    return x

def fun01():
    my_list = [5,12,15]
    print(my_list)		
    my_list = list(map(addBy10,my_list))
    print(my_list)	

fun01()
