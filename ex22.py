
# filtering a string by certain characters and inserting into set
def fun01():
    setObj = set() # instiatiating set object
    str = 'abracadabra'
    
    for x in str:
        if x not in 'abc':
            setObj.add(x)

    print("original string : \"",str,"\", Filtered ",setObj)

fun01()


# filtering a string by certain characters and inserting into sets
# the operation done in 'fun01' is done in 'fun02' using inline looping
def fun02():
    setObj = {x for x in 'zvatsqtvqvqsqsxc' if x not in 'vtxqs'}
    print("original string : \"zvatsqtvqvqsqsxc\", Filtered ",setObj)

fun02()
