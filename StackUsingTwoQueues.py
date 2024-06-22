#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
# Push -> O(n)
# Pop -> O(1)
from queue import Queue   
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    while not queue_1.empty():
        queue_2.put(queue_1.get())
    
    queue_1.put(x)
    while not queue_2.empty():
        queue_1.put(queue_2.get())


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    # code here
    if queue_1.empty():
        return -1
    else:
        return queue_1.get()
