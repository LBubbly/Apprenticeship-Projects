import csv 
from lists import * 
from os import system 
#---------------------------------------------------------------------------------  


class Employee:       

    def __init__(self, emp_id, emp_first_name, emp_last_name,  
                 emp_age, birth_date, join_date, emp_salary,  
                 emp_manager_name, dep_name):   
        self.emp_id = emp_id   
        self.emp_first_name = emp_first_name   
        self.emp_last_name = emp_last_name   
        self.emp_age = emp_age  
        self.birth_date = birth_date   
        self.join_date = join_date                        
        self.emp_salary = emp_salary                  
        self.emp_manager_name = emp_manager_name   
        self.dep_name = dep_name         


#---------------------------------------------------------------------------------  
 

def main(): 

    print('***************************', 
          '*   WANNA GENERATE 100?   *', 
          '***************************\n', 
          '(Y) Yes', 
          '(N) No\n', 
          sep='\n') 
 
    user_input = input('Choose [Y|N]: ') 
    match user_input.upper(): 
        case 'Y': 
            system('cls') 
            generate() 
            print('Boom*', 
                  '(You\'re Welcome)', 
                  sep='\n') 
            do_again() 
        case 'N': 
            system('cls') 
            print('Maybe next time...') 
            exit(0) 
        case default: 
            system('cls') 
            print('INVALID INPUT - TRY AGAIN') 
            main() 
 

#---------------------------------------------------------------------------------  


def do_again(): 

    print('\nGenerate Again?', 
          '(Y) Yes', 
          '(N) No', 
          sep='\n') 

    y_or_n_input = input('Select [Y|N]: ') 
    match y_or_n_input.upper(): 
        case 'Y': 
            system('cls') 
            generate() 
            do_again() 
        case 'N': 
            system('cls') 
            print('Guess we\'re done for today... Good work!!!') 
            exit(0) 
        case default: 
            system('cls') 
            print('INVALID INPUT!') 
            do_again() 

 
#---------------------------------------------------------------------------------  


def generate(): 
    
    ids_list = [] 
    random_id_generator(ids_list) 


    first_names_list = [] 
    last_names_list = [] 
    manager_names_list = [] 
    name_generator(first_names_list) 
    name_generator(last_names_list, first_names_list) 
    name_generator(manager_names_list, first_names_list, last_names_list) 

 
    ages_list = [] 
    birth_dates_list = [] 
    join_dates_list = [] 
    age_n_dates(ages_list, birth_dates_list, join_dates_list) 


    salaries_list = [] 
    random_salaries(salaries_list) 


    departments_list = ['Finance', 'Marketing', 'Human Resources',  
                        'Sales', 'IT', 'Customer Service', 'Legal',  
                        'Operations', 'Research and Development',  
                        'Product Management']  
    random_department(departments_list) 


    #------------------------------------------------------------ 


    employees_list = [] 
    count = 0  
    while len(employees_list) < 100:    
        employees_list.append( 
                       Employee(ids_list[count], 
                                first_names_list[count], 
                                last_names_list[count], 
                                
                                ages_list[count], 
                                birth_dates_list[count], 
                                join_dates_list[count], 

                                salaries_list[count], 
                                manager_names_list[count], 
                                departments_list[count])) 

        count += 1 


    #------------------------------------------------------------ 


    with open('employee-data.csv', mode='w', newline='') as file: 
        writer = csv.writer(file) 
        writer.writerow(['Employee Id', 'First Name', 'Last Name',  
                         'Age', 'Birth Date', 'Join Date',  
                         'Salary', 'Manager Name', 'Department']) 

        for employee in employees_list: 
            writer.writerow([employee.emp_id, employee.emp_first_name, employee.emp_last_name,  
                            employee.emp_age, employee.birth_date, employee.join_date,  
                            employee.emp_salary, employee.emp_manager_name, employee.dep_name]) 


#---------------------------------------------------------------------------------  
main() 