from logging_details.logger_class import log
from config.access_properties import property
from .file_operations.csv_operations import CSVOperations_Gen
from .file_operations.json_operations import JSONOperations_Gen


class GeneratorProgram:

    def csv_or_json_display(self):
        try:
            log.info(f'Started Execution: {self.csv_or_json_display.__name__} (Class: {GeneratorProgram.__name__})')
            print('in csv_or_json_display')
            
            selected_file_format = input(f"{property.access_displays('type_of_file_generator_display')} ")
            match selected_file_format:
                case '1':
                    selected_file_format = 'csv'
                case '2':
                    selected_file_format = 'json'
                case '3':
                    selected_file_format = 'both'
                case default:
                    print(f'INVALID INPUT: {selected_file_format}')
                    self.csv_or_json_display()

            return selected_file_format
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.csv_or_json_display.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.csv_or_json_display.__name__}')
            



    def emp_or_dept_display(self):
        try:
            log.info(f'Started Execution: {self.emp_or_dept_display.__name__} (Class: {GeneratorProgram.__name__})')
            
            selected_data_type = input(f"{property.access_displays('type_of_data_display')} ")
            match selected_data_type:
                case '1':
                    selected_data_type = 'employee'
                    return selected_data_type
                case '2':
                    selected_data_type = 'department'
                    return selected_data_type
                case '3':
                    selected_data_type = 'both'
                    return selected_data_type
                case default:
                    print(f'INVALID INPUT: {selected_data_type}')
                    self.emp_or_dept_display()
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.emp_or_dept_display.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.emp_or_dept_display.__name__}')


    def select_total_object_number(self):
        try:
            log.info(f'Started Execution: {self.select_total_object_number.__name__} (Class: {GeneratorProgram.__name__})')
            number_of_objects = int(input(f"{property.access_displays('number_of_rows_to_generate')} "))
            return number_of_objects
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.select_total_object_number.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.select_total_object_number.__name__}')


    def generator_selector(self, selected_file_format, selected_data_type):
        try:
            log.info(f'Started Execution: {self.generator_selector.__name__} (Class: {GeneratorProgram.__name__})')
            
            csv_gen_ops = CSVOperations_Gen()
            json_gen_ops = JSONOperations_Gen()

            number_of_objects = 0
            if selected_data_type in ('employee', 'both'):
                number_of_objects = self.select_total_object_number()

            match selected_file_format:
                case 'csv':
                    csv_gen_ops.generate_to_csv(selected_data_type, number_of_objects)
                case 'json':
                    json_gen_ops.generate_to_json(selected_data_type, number_of_objects)
                case 'both':
                    csv_gen_ops.generate_to_csv(selected_data_type, number_of_objects)
                    json_gen_ops.generate_to_json(selected_data_type, number_of_objects)
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.generator_selector.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.generator_selector.__name__}')


