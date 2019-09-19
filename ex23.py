
def fun01():
    # intialising dictionary
    tel = {
        'jack' : 2341,
        'ron' : 4356,
        'swet' : 1265
    }

    print(tel)

    # iterating through dictionary
    for nm in tel:
        print(nm)	

    # getting only the list of keys from dictionay
    keys = list(tel)    
    print(keys)

fun01()
