import threading as th
import random as r
import time as t

#----------------------------------------------------------

def main():
    
    print('******************************',
          '*    WELCOME TO THE STORE!   *',
          '******************************',
          sep='\n')
    
    store = []
    
    i_amount = int(input('Enter item amount: '))
    n_producers = int(input('Enter amount of producer threads: '))
    n_consumers = int(input('Enter amount of consumer threads: '))
    
    
    print(f'Main: Ready to produce {i_amount} items.')
    
    
    p_count = 0
    producers = []
    for p in range(n_producers):
        print(f'Main: Started Producer {p_count}')
        producer_thread = th.Thread(target=Monitor.producer, args=(i_amount, store, p_count))
        producers.append(producer_thread)
        producer_thread.start()
        p_count += 1
        
    c_count = 0
    consumers = []
    for c in range(n_consumers):
        print(f'Main: Started Consumer {c_count}')
        consumer_thread = th.Thread(target=Monitor.consumer, args=(i_amount, store, c_count))
        consumers.append(consumer_thread)
        consumer_thread.start()
        c_count += 1
    
    
    t.sleep(1)
    p_joining = 0  
    for p in producers:
        print(f'Main: Producer {p_joining} Joined.')
        p.join()
        p_joining += 1    
    
    c_joining = 0        
    for c in consumers:
        print(f'Main: Consumer {c_joining} Joined.')        
        c.join()
        c_joining += 1
        
        
    print('Main Program Complete')


class Monitor:
    
    def producer(amount, store_q, count):        
        i = 0
        
        while i < amount: 
            t.sleep(r.randint(0, 2))
            item = r.randint(1, 100)
            store_q.append(item)
            i += 1
            
        print(f'P{count} Total Items Produced: {amount} (Thread Finished)')
        

    def consumer(amount, store_q, count):
        i = 0
        i_consumed = 0
        consumed_val = []
        
        while i < amount:
            t.sleep(r.randint(1, 3))
        
            if len(store_q) == 0:
                print('Store is empty, please wait...')
                t.sleep(3)
                if len(store_q) == 0:
                    print('Store is empty. We\'re sold out. (Thread Finished)')
                    break
                
            item = store_q.pop(0)
            consumed_val.append(item) 
            
            s_len = len(store_q)
            cv_len = len(consumed_val)
            if s_len > 0 and s_len > cv_len:
                total = s_len - cv_len
                print(f'C{count}: Writing {s_len} - {cv_len} = {total} left')
            
            i += 1
            i_consumed += 1
            
        print(f'C{count}: Total Amount Consumed: {i_consumed}')

#----------------------------------------------------------

main()