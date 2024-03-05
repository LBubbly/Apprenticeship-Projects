'''
def generate(choice, number_of_rows):
    employees_list = []
    match choice:
        case 'csv':
            to_csv(lists_to_emp_obj(employees_list, number_of_rows))
        case 'json':
            to_json(lists_to_emp_obj(employees_list, number_of_rows))
        case 'both':
            to_csv(lists_to_emp_obj(employees_list, number_of_rows))
            to_json(lists_to_emp_obj(employees_list, number_of_rows))
'''