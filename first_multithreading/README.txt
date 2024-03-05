This README is meant for "main.py" 
(Note: the other "main#.py" files are random attempts and experiments)

Hello, this is my Producer-Consumer Multithreading Model.

Running the program is simple. Simply start the program, enter the necessary inputs and the program will automatically do the rest.


------------------------ About main() ------------------------

- I defined the shared queue called 'store' and made it a list.

- I created 3 inputs and stored them inside a variable:
    - 1, Collects the item amount
    - 1, Collects the amount of producer threads
    - 1, Collects the amount of consumer threads

- I created a for loop to create and start the specified number of threads entered by the user for both the producer and consumer threads.

- I created a for loop to label and join the threads when they are finished execution.

- I printed 'Main Program Complete' so the user knows when the main() program is finished.

------------------------ About Monitor Class ------------------------

- I created and defined 2 methods: 
    
    - producer(), 
        - This method's purpose is to take the amount of items entered by the user, the shared store queue, and the producer count (E.g. P0, P1..) and then create and append items to the shared queue.
        - Once the producer has produced the specified amount of items, it prints the amount produced and clarifies that the thread is finished.        -

    - consumer(), 
        - This method's purpose is to take the amount of items entered by the user, the shared store queue, and the consumer count (E.g. C0, C1..) and then consume and pop items from the shared queue. 
        - This method writes the total amount of products being consumed during each iteration.
        - This method double checks whether the shared queue is empty before finishing the thread.
        - Once the consumer has consumed all of the items produced, it prints the total amount consumed.