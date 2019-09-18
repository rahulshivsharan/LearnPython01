def fun01():
    basket = {"ONE", "TWO", "THREE"}
    basket.add("ONE") # no duplicates allowed
    basket.add("FOUR")
	
    for x in basket:	
        print("ELEMENT ",x)
    
fun01()
