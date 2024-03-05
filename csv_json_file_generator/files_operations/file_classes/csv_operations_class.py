import csv
# import pandas as pd
from files_operations.db_utilities.postgres_utility import PostGres
from generator_operations.generator_classes.generators_class import Generators


class CSVOperations:
    def __init__(self):
        self.employee_csv_file_path = 'generator_operations\generated_data\employee_generated_data\employee_data.csv'
        self.department_csv_file_path = 'generator_operations\generated_data\department_generated_data\department_data.csv'
    
    def generate_emps_to_csv(self, employees_list):
        try:
            with open(self.employee_csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                                 # Adjust to change
                writer.writerow(['emp_id', 'first_name', 'last_name', 'age', 'birth_date', 'join_date',
                                 'salary', 'manager', 'department'])

                for employee in employees_list:
                    writer.writerow([employee.emp_id, employee.emp_first_name, employee.emp_last_name,
                                     employee.emp_age, employee.birth_date, employee.join_date,
                                     employee.emp_salary, employee.emp_manager_name, employee.dept_name])
        except:
            pass
        else:
            print('Successful Generation to Employee CSV File!')




    def generate_depts_to_csv(self, departments_list):
        try:
            with open(self.department_csv_file_path, mode='w',
                      newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['dept_id', 'dept_name'])

                for department in departments_list:
                    writer.writerow([department.dept_id, department.dept_name])

        except:
            pass
        else:
            print('Successful Generation to Department CSV File!')




    def generate_to_csv(self, choice, number_of_objects=50):
        try:
            generator = Generators()

            match choice.lower():
                case 'employee':
                    self.generate_emps_to_csv(generator.employee_object_generator(number_of_objects))
                case 'department':
                    self.generate_depts_to_csv(generator.department_object_generator())
                case 'both':
                    self.generate_emps_to_csv(generator.employee_object_generator(number_of_objects))
                    self.generate_depts_to_csv(generator.department_object_generator())
        except:
            pass
        else:
            print('CSV Success!!!')




    def read_csv_to_postgres(self, connection, cursor, table_query, table_name):
        try:
            match table_name.lower():
                case 'employee':
                     
            
            
            with open('', 'r') as file:
        
                reader = csv.reader(file)    
                header = next(reader)

                cursor.execute(table_query)
                connection.commit()

                insert_query = f"INSERT INTO {table_name} ({','.join(header)}) VALUES ({','.join(['%s']*len(header))})"
                for row in reader:
                    cursor.execute(insert_query, row)
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


    def pandas_read_csv(self):
        try:
            pass
        except:
            pass
        else:
            pass

# csv_ops = CSVOperations()
# csv_ops.generate_to_csv('department', 10)