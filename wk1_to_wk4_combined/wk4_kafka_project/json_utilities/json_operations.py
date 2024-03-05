import json
from logging_details.logger_class import log
from config.access_properties import property  
from wk1_generator.generator_classes.generators_class import Generators


class JSONOperations_Gen:
    def __init__(self):
        self.emp_column_names = ['emp_id', 'first_name', 'last_name', 'age', 'birth_date', 'join_date', 'salary', 'manager', 'department']
        self.dept_column_names = ['dept_id', 'dept_name']
    
    
    def generate_emps_to_json(self, employees_list):
        # print('in generate_emps_to_json')
        try:
            log.info(f'Started Execution: {self.generate_emps_to_json.__name__} (Class: {JSONOperations_Gen.__name__})')
            
            for_json = []
            emp_columns = self.emp_column_names
            for employee in employees_list:
                for_json.append({
                    f"{emp_columns[0]}": employee.emp_id,
                    f"{emp_columns[1]}": employee.emp_first_name,
                    f"{emp_columns[2]}": employee.emp_last_name,
                    f"{emp_columns[3]}": employee.emp_age,
                    f"{emp_columns[4]}": employee.birth_date.isoformat(),
                    f"{emp_columns[5]}": employee.join_date.isoformat(),
                    f"{emp_columns[6]}": employee.emp_salary,
                    f"{emp_columns[7]}": employee.emp_manager_name,
                    f"{emp_columns[8]}": employee.dept_name
                })

            with open(f"{property.access_pg_sql_file('employee_json_file_path')}", 'w') as file:
                json.dump(for_json, file, indent=4)
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.generate_emps_to_json.__name__}, ERROR: {e}')
        else:
            log.info('Successful Generation to Employee JSON File!')
        finally:
            log.info(f'Finished Execution: {self.generate_emps_to_json.__name__}')
        
        

    def generate_depts_to_json(self, department_list):
        try:
            log.info(f'Started Execution: {self.generate_depts_to_json.__name__} (Class: {JSONOperations_Gen.__name__})')
            
            # print('in generate_depts_to_json')
            for_json = []
            dept_columns = self.dept_column_names
            for department in department_list:
                for_json.append({
                    f"{dept_columns[0]}": department.dept_id,
                    f"{dept_columns[1]}": department.dept_name
                })

            with open(f"{property.access_pg_sql_file('department_json_file_path')}", 'w') as file:
                json.dump(for_json, file, indent=4)
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.generate_depts_to_json.__name__}, ERROR: {e}')
        else:
            log.info('Successful Generation to Department JSON File!')
        finally:
            log.info(f'Finished Execution: {self.generate_depts_to_json.__name__}')




    def generate_to_json(self, selected_data_type, number_of_objects=0):
        try:
            log.info(f'Started Execution: {self.generate_to_json.__name__} (Class: {JSONOperations_Gen.__name__})')
            
            generator = Generators()

            match selected_data_type.lower():
                case 'employee':
                    self.generate_emps_to_json(generator.employee_object_generator(number_of_objects))
                case 'department':
                    self.generate_depts_to_json(generator.department_object_generator())
                case 'both':
                    self.generate_emps_to_json(generator.employee_object_generator(number_of_objects))
                    self.generate_depts_to_json(generator.department_object_generator())
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.generate_to_json.__name__}, ERROR: {e}')
        else:
            log.info('JSON Success!')
        finally:
            log.info(f'Finished Execution: {self.generate_to_json.__name__}')

