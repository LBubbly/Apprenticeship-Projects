'''
Genuinely experimenting, definitely aware that the way this program is NOT written following best practices - BUT - Was this fun? 
I say, HECK YEAHHHH!!! 

'''


import threading
import time
import random

shared_q = []
p_count = 0
c_count = 0

# producer_thread_default = 1
# i_consumed = 0 ...more functionality


#-------------------------------------------------------------

i_amount = int(input('Enter item amount: '))
n_producers = int(input('Enter amount of producer threads: '))
n_consumers = int(input('Enter amount of consumer threads: '))

#-------------------------------------------------------------

def producer():
    print(f'Main: Started Producer {p_count}')
    i = 0
    while i < i_amount:
        time.sleep(random.randint(0,2))
        item = random.randint(1, 100)
        shared_q.append(item)
        print(f'P{p_count} Produced: {item}')
        i += 1
    print(f'P{p_count} Items Produced: {shared_q}',
          f'P{p_count} Amount Produced: {len(shared_q)}/{i_amount}',
          sep='\n')

#-------------------------------------------------------------

def consumer():
    print(f'Main: Started Consumer {c_count}')
    i = 0
    i_consumed = 0
    while i < i_amount:
        time.sleep(random.randint(1,3))
        
        
        if len(shared_q) == 0:
            print('Queue is empty.')
            time.sleep(3)
            
            if len(shared_q) == 0:
                break
        
        item = shared_q.pop(0)
        print(f'C{c_count} Consumed: {item}')
        i += 1
        i_consumed += 1
    

    print(f'C{c_count} Total Amount Consumed: {i_consumed}')

#-------------------------------------------------------------


producers = []
for p in range(n_producers):
    producer_thread = threading.Thread(target=producer)
    producers.append(producer_thread)
    producer_thread.start()
    p_count += 1
    
    
consumers = []
for c in range(n_consumers):
    consumer_thread = threading.Thread(target=consumer)
    consumers.append(consumer_thread)
    consumer_thread.start()
    c_count += 1
    
for p in producers:
    p.join()
    
for c in consumers:
    c.join()
    
print('Main Program Complete')