import psycopg2

class PostGres:
    def __init__(self):
        self.pg_host_name = 'localhost'
        self.pg_port = '5432'
        self.pg_database = 'employee_db'
        self.pg_username = 'postgres'
        self.pg_password = 'postpass'

        # Place SQL in separate class after successful load -------------------------
        self.emp_table_name = 'employee'
        self.emp_column_names = [['emp_id', 'VARCHAR(10)'], 
                                 ['first_name', 'CHAR(10)'],
                                 ['last_name', 'CHAR(10)'], 
                                 ['age', 'INT'], 
                                 ['birth_date', 'DATE'],
                                 ['join_date', 'DATE'],
                                 ['salary', 'INT'], 
                                 ['manager', 'CHAR(5)'],
                                 ['department', 'CHAR(30)']]
        self.dept_table_name = 'department'
        self.dept_column_names = [['dept_id', 'VARCHAR(10)'], 
                                  ['dept_name', 'CHAR(30)']]
        self.query_create_employee_table = \
            f'''DROP TABLE IF EXISTS {self.emp_table_name};
            CREATE TABLE IF NOT EXISTS {self.emp_table_name}(
                {self.emp_column_names[0][0].lower()} {self.emp_column_names[0][1].upper()} PRIMARY KEY,
                {self.emp_column_names[1][0].lower()} {self.emp_column_names[1][1].upper()},
                {self.emp_column_names[2][0].lower()} {self.emp_column_names[2][1].upper()},
                {self.emp_column_names[3][0].lower()} {self.emp_column_names[3][1].upper()},
                {self.emp_column_names[4][0].lower()} {self.emp_column_names[4][1].upper()},
                {self.emp_column_names[5][0].lower()} {self.emp_column_names[5][1].upper()},
                {self.emp_column_names[6][0].lower()} {self.emp_column_names[6][1].upper()},
                {self.emp_column_names[7][0].lower()} {self.emp_column_names[7][1].upper()},
                {self.emp_column_names[8][0].lower()} {self.emp_column_names[8][1].upper()});'''
        self.query_create_department_table = \
            f'''DROP TABLE IF EXISTS {self.dept_table_name};
            CREATE TABLE IF NOT EXISTS {self.dept_table_name}(
                {self.dept_column_names[0][0].lower()} {self.dept_column_names[0][1].upper()} PRIMARY KEY,
                {self.dept_column_names[1][0].lower()} {self.dept_column_names[1][1].upper()};'''
    #-------------------------------------------------------------------------------------------------------


    def file_to_db(self, file_type, file_func, type_of_data):
        try:
            connection = psycopg2.connect(
                host = self.pg_host_name,
                port = self.pg_port,
                database = self.pg_database,
                user = self.pg_username,
                password = self.pg_password
            )
            cursor = connection.cursor()

            table_query = ''
            match type_of_data:
                case self.emp_table_name:
                    table_query = self.query_create_employee_table
                case self.dept_table_name:
                    table_query = self.query_create_department_table

            try:
                file_func(connection, cursor, table_query, type_of_data)
            except:
                pass
            else:
                print(f'Successfully Loaded the {file_type.upper()}!')
            finally:
                cursor.close()
                connection.close()

        except:
            print('File To DB: Failed')
        else:
            print('File to DB: Succeeded')


pg = PostGres()
print(pg.query_create_employee_table,
    pg.query_create_department_table,
    sep='\n')