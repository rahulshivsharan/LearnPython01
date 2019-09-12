
def sqr(x):
    return x**2

def fun01():
    sq_list = list(map(sqr,range(5))) # applying function on each element present in range (here the function is square of number)
    print(sq_list)	

fun01()
