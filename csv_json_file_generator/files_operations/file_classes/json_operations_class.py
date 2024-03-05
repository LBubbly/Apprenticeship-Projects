import json
# import pandas as pd
from files_operations.db_classes.postgres_class import PostGres
from generator_operations.generator_classes.generators_class import Generators

class JSONOperations:
    def __init__(self):
        self.employee_json_file_path = 'generator_operations\generated_data\employee_generated_data\employee-data.json'
        self.department_json_file_path = 'generator_operations\generated_data\department_generated_data\department-data.json'
    
    def generate_emps_to_json(self, employees_list):
        try:
            for_json = []
            for employee in employees_list:
                for_json.append({
                    'emp_id': employee.emp_id,
                    'first_name': employee.emp_first_name,
                    'last_name': employee.emp_last_name,
                    'age': employee.emp_age,
                    'birth_date': employee.birth_date.isoformat(),
                    'join_date': employee.join_date.isoformat(),
                    'salary': employee.emp_salary,
                    'manager': employee.emp_manager_name,
                    'department': employee.dept_name
                })

            with open(self.employee_json_file_path, 'w') as file:
                json.dump(for_json, file, indent=4)
        except:
            pass
        else:
            print('Successful Generation to Employee JSON File!')


    def generate_depts_to_json(self, department_list):
        try:
            for_json = []
            for department in department_list:
                for_json.append({
                    'dept_id': department.dept_id,
                    'dept_name': department.dept_name
                })

            with open(self.department_json_file_path, 'w') as file:
                json.dump(for_json, file, indent=4)
        except:
            pass
        else:
            print('Successful Generation to Department JSON File!')





    def generate_to_json(self, selected_data_type, number_of_objects=0):
        try:
            generator = Generators()

            match selected_data_type.lower():
                case 'employee':
                    self.generate_emps_to_json(generator.employee_object_generator(number_of_objects))
                case 'department':
                    self.generate_depts_to_json(generator.department_object_generator())
                case 'both':
                    self.generate_emps_to_json(generator.employee_object_generator(number_of_objects))
                    self.generate_depts_to_json(generator.department_object_generator())
        except:
            pass
        else:
            print('JSON Success!!!')


# -----------------------------------


    def read_json_to_postgres(self, connection, cursor, table_query, table_name):
        try:
            
            with open('', 'r') as file:
            
                json_data = json.load(file)
                keys = list(json_data[0].keys())
                cursor.execute(table_query)
                connection.commit()

                for obj in json_data:
                    values = [obj[key] for key in keys]
                    insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(values))})"
                    cursor.execute(insert_query, values)

            connection.commit()
        except:
            pass
        else:
            pass


    def json_to_postgres(self):
        try:
            pass
        except:
            pass
        else:
            pass
    


    def pandas_read_json(self):
        try:
            pass
        except:
            pass


# json_ops = JSONOperations()
# json_ops.generate_to_json('both', 5)
