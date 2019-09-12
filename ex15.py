from collections import deque

def fun01():
    queue = deque(["ONE","TWO","THREE"])
    print(queue)
    print("1st pop from left ",queue.popleft())
    print("after pop ",queue)
    queue.append("FOUR")
    print("after append ",queue)	
    print("2nd pop from left ",queue.popleft())
    print("after pop ",queue)
    queue.append("FIVE")
    print("after append ",queue)	

fun01()
