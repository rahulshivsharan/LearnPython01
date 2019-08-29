def func():
    my_stack = []
	
    my_stack.append("ONE")
    my_stack.append("TWO")
    my_stack.append("THREE")
    my_stack.append("FOUR")	
	
    while len(my_stack) != 0:
        print("POP ",my_stack.pop())

func()		
