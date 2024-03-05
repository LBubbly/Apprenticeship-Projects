from os import system 
from math import floor, pi 
#---------------------------------------------------------------------------------  


random_numbers = []  
changing_number = 0  

def pseudo_random(seed):  
    global random_numbers  
    global changing_number  

    if len(random_numbers) == 10:  
        print(f'List: {random_numbers}')  
        return random_numbers  
    else:  
        changing_number = floor((seed * 8) % 11) 
        random_numbers.append(changing_number)  
        return pseudo_random(changing_number)  


#---------------------------------------------------------------------------------   
 

pi_random_numbers = [] 

def pi_pseudo_random(seed): 
    global pi_random_numbers 

    pi_times_seed_no_decimal = pi * seed 
    str_changed_pi = str(pi_times_seed_no_decimal) 
    print(f'PI * SEED = {str_changed_pi}') 

    for i in str_changed_pi: 
        if i == '.': 
            continue 

        number = int(i) 
        pi_random_numbers.append(number) 

    return pi_random_numbers 
 

#---------------------------------------------------------------------------------  


def print_results(numbers_list): 

    print('******** RESULTS BELOW ********') 
    
    for num in numbers_list: 
        print(f'              {num}') 


#---------------------------------------------------------------------------------  


def menu_return(): 

    print('Shall we return to the main menu?', 
          '1) Yes', 
          '2) No', 
          sep='\n') 

    return_input = int(input('Select [1|2]: ')) 
    match return_input: 
        case 1: 
            system('cls') 
            main() 
        case 2: 
            system('cls') 
            print('Well, that was random...', 
                  '[Exited]', 
                  sep='\n') 
            exit(0) 
        case default: 
            system('cls') 
            print('INVALID INPUT - TRY AGAIN') 
            menu_return() 
 

#---------------------------------------------------------------------------------  


def main(): 

    print('***************************************', 
          '*   SELECT A METHOD OF RANDOMNESS...  *', 
          '***************************************\n', 
          '1) Cheap Trick', 
          '2) 10 Pseudo Random Numbers', 
          '3) Exit\n', 
          sep='\n') 


    selected_method = int(input('Select [1|2|3]: ')) 
    if selected_method == 1 or selected_method == 2: 
        user_number = float(input('Number Please: ')) 
        

    match selected_method: 
        case 1: 
            system('cls') 
            pi_pseudo_random(user_number) 
            print_results(pi_random_numbers) 
            menu_return() 
        case 2: 
            system('cls') 
            pseudo_random(user_number) 
            print_results(random_numbers)  
            menu_return() 
        case 3: 
            system('cls') 
            print('Seize the day and don\'t forget the boba!!!') 
            exit(0) 
        case default: 
            system('cls') 
            print('INVALID INPUT - TRY AGAIN') 
            main() 


#---------------------------------------------------------------------------------  

main()   