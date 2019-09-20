
def scope_test():
    def do_local():
        test_str = "Local Scope"

    def do_nonlocal():
        nonlocal test_str # applying non local scope
        test_str = "Non Local scope"
		
    def do_global():
        global test_str # applying global scope
        test_str = "Global Scope"

    test_str = "Test scope"
	
    do_local()
    print("After calling method 'do_local' value of \"test_str\" : ",test_str)
	
    do_nonlocal()
    print("After calling method 'do_nonlocal' value of \"test_str\" : ",test_str)
	
    do_global()
    print("After calling method 'do_global' value of \"test_str\" : ",test_str)
	
scope_test()
