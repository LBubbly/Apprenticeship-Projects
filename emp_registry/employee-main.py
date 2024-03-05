import json
from os import system

#..................................................................

class Employee:
    
    def __init__(self, employee_id, employee_name, department_name, manager, phone_number):
        self.employee_id = employee_id,
        self.employee_name = employee_name
        self.department_name = department_name
        self.manager = manager
        self.phone_number = phone_number

    def input_to_dict(self, employee_id, employee_name, department_name, manager, phone_number):
        return {
            'id': employee_id,
            'employee_name': employee_name,
            'department': {
                'department_name': department_name,
                'manager': manager,
                'phone number': phone_number
            }
        }

    def add_data(self, employee_id, employee_name, department_name, manager, phone_number):
        with open('employee-data.json', 'r') as j_file:
            j_data = json.load(j_file)
            
        emp_dict = self.input_to_dict(employee_id, employee_name, department_name, manager, phone_number)
        j_data.append(emp_dict)
        
        with open('employee-data.json', 'w') as j_file:
            json.dump(j_data, j_file, indent=4)
            
#..................................................................

def menu_return():
    system('cls')
    
    print('Would you like to return to the main menu?',
          '1. Yes',
          '2. No',
          sep='\n')
    ch = int(input("Choose [1|2]: "))
    
    match ch:
        case 1:
            system('cls')
            main()
        case 2:
            system('cls')
            print('You have exited the Employee Registry.',
               'Have a good day!',
               sep='\n')
            exit(0)
        case default:
            print("INVALID INPUT.")
            menu_return()

#..................................................................

def employee_search(selected_search, search_criteria):    
    
    with open('employee-data.json', 'r') as j_file:
        emp_data = json.load(j_file)
    
    ss_list = []
    for item in emp_data:
        if selected_search in item:
            ss_list.append(item[selected_search])
    
    sc_list = list(filter(lambda item: search_criteria in item, ss_list))
    
    print(sc_list)
    print('Selected Search:', selected_search)
    print('Search Criteria:', search_criteria)

#..................................................................

def department_search(selected_search, search_criteria):
    
    # Isolate department dictionary from the json data
    d_list = []
    with open('employee-data.json', 'r') as j_file:
        dep_data = json.loads(j_file.read())
        for d in dep_data:
            d_list.append(d['department'])
    
    
    ssd_list = []
    for s in d_list:
        ssd_list.append(s[selected_search])
        
        
    scd_list = list(filter(lambda item: search_criteria in item, ssd_list))
    
    print(scd_list)
    print('Selected Search:', selected_search)
    print('Search Criteria:', search_criteria)
    
#..................................................................

def update_now(id, choice, change):
    
    with open('employee-data.json', 'r') as j_file:
        d_data = json.loads(j_file.read())
        for d in d_data:
            d_copy = d.copy()
            if d_copy['id'] == id.upper():
                d_copy['department'][choice] = change
                print('Changed to:', d_copy)
    
    with open('employee-data.json', 'w') as j_file:
        json.dump(d_data, j_file, indent=4)
            
 #..................................................................
            
def update_details(id):
    
    print('What would you like to update?',
          '1. Department Name',
          '2. Manager',
          '3. Phone Number\n',
          sep='\n')

    update_choice = int(input('Choose [1|2|3]: '))
    update_change = input('Update Change: ')
    
    print('Your Update Choice:', update_choice)
    print('Your Update Change:', update_change)
    
    print('Are you sure?',
          '1. Yes',
          '2. No',
          sep='\n')
    
    y_or_n = int(input('Select [1|2]: '))
    print(y_or_n)
    
    match y_or_n:
        case 1:
            
            match update_choice:    
                case 1: 
                    update_now(id, 'department_name', update_change)
                case 2: 
                    update_now(id, 'manager', update_change)
                case 3: 
                    update_now(id, 'phone number', update_change)
                case default:
                    system('cls')
                    print('INVALID INPUT')
                    update_details(id)
                
        case 2:
            system('cls')
            update_details(id)
        
        case default:
            system('cls')
            print('INVALID INPUT')
            update_details(id)

#..................................................................

def do_again(func):
    match func:
        
        case 'write':
            print('Would you like to add another employee?',
                  '1. Yes',
                  '2. No',
                  sep='\n')
            selection = int(input('Select [1|2]: '))
            match selection:
                case 1:
                    system('cls')
                    write()
                case 2:
                    system('cls') 
                    menu_return()
                case default:
                    print('INVALID INPUT.')
                    do_again('write')
                        
        case 'search':
            print('Would you like to make another search?',
                  '1. Yes',
                  '2. No',
                  sep='\n')
            selection = int(input('Select [1|2]: '))
            match selection:
                case 1:
                    system('cls')
                    search()
                case 2: 
                    system('cls')
                    menu_return()
                case default:
                    system('cls')
                    print('INVALID INPUT.')
                    do_again('search')
            
        case 'update':
            print('Would you like to update another employee\'s data?',
                  '1. Yes',
                  '2. No',
                  sep='\n')
            selection = int(input('Select [1|2]: '))
            match selection:
                case 1:
                    system('cls')
                    update()
                case 2: 
                    system('cls')
                    menu_return()
                case default:
                    system('cls')
                    print('INVALID INPUT.')
                    do_again('update')
            
        case default:
            system('cls')
            print('INVALID INPUT.')
            match func:
                case 'write':
                    do_again('write')
                case 'search': 
                    do_again('search')
                case 'update': 
                    do_again('update')
                case default:
                    system('cls')
                    print('Returning to the main menu...')
                    menu_return()
                    
#..................................................................

def write():
    
    print('*********************************',
          '*         ADD EMPLOYEE:         *',
          '*********************************\n',
          sep='\n')
    
    new_id, new_name, dep_name, manager_name, ph_num = \
        input('ID: '), input('Employee Name: '), input('Department Name: '), input('Manager Name: '), input('Phone Number: ')
    
    ne_data = Employee(new_id.upper(), new_name, dep_name, manager_name, ph_num)
    
    ne_data.add_data(new_id.upper(), new_name, dep_name, manager_name, ph_num)
    
    do_again('write')

#..................................................................

def search(): 
    
    print('********************************',
          '*       SEARCH EMPLOYEE:       *',
          '********************************\n',
          sep='\n')
    
    print('Search by:',
          '1. Employee ID',
          '2. Employee Name',
          '3. Department Name',
          '4. Manager',
          '5. Phone Number\n',
          sep='\n')

    search_by = int(input('Choose [1|2|3|4|5]: '))
    
    match search_by:
        case 1:
            search_criteria = input('\nSearch Criteria: ')
            employee_search('id', search_criteria.upper())
        case 2: 
            search_criteria = input('\nSearch Criteria (Case Sensitive): ')
            employee_search('employee_name', search_criteria)
        case 3:
            search_criteria = input('\nSearch Criteria (Case Sensitive): ')
            department_search('department_name', search_criteria)
        case 4:
            search_criteria = input('\nSearch Criteria (Case Sensitive): ')
            department_search('manager', search_criteria)
        case 5: 
            search_criteria = input('\nSearch Criteria: ')
            department_search('phone number', search_criteria)
        case default:
            system('cls')
            print('INVALID INPUT.')
            search()
    
    do_again('search')
    
#..................................................................

def update():
    
    print('********************************',
          '*       UPDATE EMPLOYEE:       *',
          '********************************\n',
          sep='\n')

    
    id_criteria = input('Employee ID Criteria: ')
    
    id_list = []
    with open('employee-data.json', 'r') as j_file:
        id_data = json.loads(j_file.read())
        for id in id_data: 
            id_list.append(id['id'])
    
    idc_list = list(filter(lambda id: id_criteria in id, id_list))
    
    print('IDC:', idc_list)
    print('Criteria:', id_criteria)
    
    full_id = input('Please enter the full id: ')
    
    target_emp = None
    for em in id_data:
        if em['id'] == full_id.upper():
            target_emp = em
            break
    
    print('Target Employee\'s Data:', target_emp)
    
    update_details(full_id)
    
    do_again('update')

#..................................................................

def main():
    print('*********************************',
          '*       EMPLOYEE REGISTRY       *',
          '*********************************\n',
          sep='\n')
    
    print('1. Add Employee',
          '2. Search Employee',
          '3. Update Employee',
          '4. Exit Program\n',
          sep='\n')

    selected = int(input('Select [1|2|3|4]: '))
    
    match selected:
        case 1:
            system('cls')
            write()
            menu_return()
        case 2:
            system('cls')
            search()
            menu_return()
        case 3:
            system('cls')
            update()
            menu_return()
        case 4:
            system("cls")
            print('Goodbye!')
            exit(0)
        case default:
            system('cls')
            print('INVALID INPUT')
            main()
    
#..................................................................

main()