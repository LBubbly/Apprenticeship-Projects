import csv
from logging_details.logger_class import log
from config.access_properties import property 
from wk1_generator.generator_classes.generators_class import Generators


class CSVOperations_Gen:
    def __init__(self):
        self.emp_column_names = ['emp_id', 'first_name', 'last_name', 'age', 'birth_date', 'join_date', 'salary', 'manager', 'department']
        self.dept_column_names = ['dept_id', 'dept_name']
        
    
    def generate_emps_to_csv(self, employees_list):
        try:
            log.info(f'Started Execution: {self.generate_emps_to_csv.__name__} (Class: {CSVOperations_Gen.__name__})')
            
            print('in generate_emps_to_csv: ', property.access_pg_sql_file('employee_csv_file_path'))
            with open(f"{property.access_pg_sql_file('employee_csv_file_path')}", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.emp_column_names)
                for employee in employees_list:
                    writer.writerow([employee.emp_id, employee.emp_first_name, employee.emp_last_name,
                                     employee.emp_age, employee.birth_date, employee.join_date,
                                     employee.emp_salary, employee.emp_manager_name, employee.dept_name])
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.generate_emps_to_csv.__name__}, ERROR: {e}')
        else:
            log.info('Successful Generation to Employee CSV File!')
        finally:
            log.info(f'Finished Execution: {self.generate_emps_to_csv.__name__}')



    def generate_depts_to_csv(self, departments_list):
        try:
            log.info(f'Started Execution: {self.generate_depts_to_csv.__name__} (Class: {CSVOperations_Gen.__name__})')
            
            print('in generate_depts_to_csv')
            with open(f"{property.access_pg_sql_file('department_csv_file_path')}", mode='w',
                      newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.dept_column_names)
                for department in departments_list:
                    writer.writerow([department.dept_id, department.dept_name])

        except Exception as e:
            log.error(f'[!!!] CHECK: {self.generate_depts_to_csv.__name__}, ERROR: {e}')
        else:
            log.info('Successful Generation to Department CSV File!')
        finally:
            log.info(f'Finished Execution: {self.generate_depts_to_csv.__name__}')



    def generate_to_csv(self, choice, number_of_objects=50):
        try:
            log.info(f'Started Execution: {self.generate_to_csv.__name__} (Class: {CSVOperations_Gen.__name__})')
            
            generator = Generators()

            match choice.lower():
                case 'employee':
                    self.generate_emps_to_csv(generator.employee_object_generator(number_of_objects))
                case 'department':
                    self.generate_depts_to_csv(generator.department_object_generator())
                case 'both':
                    self.generate_emps_to_csv(generator.employee_object_generator(number_of_objects))
                    self.generate_depts_to_csv(generator.department_object_generator())
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.generate_to_csv.__name__}, ERROR: {e}')
        else:
            log.info('CSV Success!')
        finally:
            log.info(f'Finished Execution: {self.generate_to_csv.__name__}')

