from files_operations.file_classes.csv_operations_class import CSVOperations
from files_operations.file_classes.json_operations_class import JSONOperations

class GeneratorProgram:

    def csv_or_json_display(self):
        try:
            print('************************************',
                  '*    GENERATE FILE: CSV OR JSON    *',
                  '************************************\n',
                  '1) CSV',
                  '2) JSON',
                  '3) BOTH',
                  '4) EXIT PROGRAM',
                  sep='\n')
            selected_file_format = input('SELECT [1|2|3|4]: ')
            match selected_file_format:
                case '1':
                    selected_file_format = 'csv'
                case '2':
                    selected_file_format = 'json'
                case '3':
                    selected_file_format = 'both'
                case '4':
                    print('You have exited the program.')
                    exit(0)
                case default:
                    print(f'INVALID INPUT: {selected_file_format}')
                    self.csv_or_json_display()

            return selected_file_format
        except:
            print('Error!!!')
        



    def emp_or_dept_display(self):
        try:
            print('\n*********************************************',
                  '*    GENERATE DATA: EMPLOYEE OR DEPARTMENT    *',
                  '***********************************************\n',
                  '1) EMPLOYEE',
                  '2) DEPARTMENT',
                  '3) BOTH',
                  '4) EXIT PROGRAM',
                  sep='\n')
            selected_data_type = input('SELECT [1|2|3|4]: ')

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
                case '4':
                    print('You have exited the program.')
                    exit(0)
                case default:
                    print(f'INVALID INPUT: {selected_data_type}')
                    self.emp_or_dept_display()
        except:
            print('Error!!!')
        



    def select_total_object_number(self):
        try:
            number_of_objects = int(input('Enter number of objects to generate: '))
            return number_of_objects
        except:
            print('Error!!!')
        



    def generator_selector(self, selected_file_format, selected_data_type):
        try:
            csv_ops = CSVOperations()
            json_ops = JSONOperations()

            number_of_objects = 0
            if selected_data_type in ('employee', 'both'):
                number_of_objects = self.select_total_object_number()

            match selected_file_format:
                case 'csv':
                    csv_ops.generate_to_csv(selected_data_type, number_of_objects)
                case 'json':
                    json_ops.generate_to_json(selected_data_type, number_of_objects)
                case 'both':
                    csv_ops.generate_to_csv(selected_data_type, number_of_objects)
                    json_ops.generate_to_json(selected_data_type, number_of_objects)
        except:
            print('Error!!!')




    def generator_program(self):
        try:
            csv_or_json = self.csv_or_json_display()
            employee_or_department = self.emp_or_dept_display()
            self.generator_selector(csv_or_json, employee_or_department)
        except:
            print('Error!!!')