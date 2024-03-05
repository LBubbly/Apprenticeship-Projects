Hi! This is my documentation for my Employee Registry system!

When the user runs the program, the main menu screen will pop up.

The user has 4 options:
    1. Add Employee - Allows the user to add a new employee and appends the data to the employee-data.json file. 
    2. Search Employee - Allows the user to search for a specific piece of information from the employee-data.json.
    3. Update Employee - Allows the user to target a specific employee's data and update any one of the department details.
    4. Exit Program - Alows the user to exit and end the program.


---------- About main() ----------

In order to select an option the user will have to type a single number [1|2|3|4]. The input will be converted to an integer since the input is wrapped by the int() type conversion function.

Depending on the input a match-case scenario will activate beginning with clearing the screen. If 1-3 is selected, the program will call each function I've built for their intend purpose. If 4 is selected, the program will say 'Goodbye!' and the program will end. If the user types in a number that is not 1-4, the program will call itself again and leave a note 'INVALID INPUT'. 

---------- About Employee Class ----------

When a new Employee object is being created, the attributes that are required aside from self is: employee_id, employee_name, department_name, manager, phone_number

I have also defined 2 methods within the class: 
    1. input_to_dict() - used to transform the object into a dictionary.
    2. add_data() - used with the write function to append the new employee dictionary to the employee-data.json

---------- About menu_return() ----------

The purpose of this function is to either return the user to the main menu or end the program.

---------- About do_again() ----------

The purpose of this function is to allow the user to perform an action again. For example, if the user would like to add 5 more employees consecutively, this function would enable them to it again without having to return to the main menu each time.

I used nested match-case scenarios for the following actions:
    1. Add Employee - write()
    2. Search Emploee - search()
    3. Update Employee - update()
    4. Default - If user submits invalid input the program will try again or automatically return the user to the main menu.

---------- About write() ----------

The purpose of this function is to add a new employee and their details to the employee-data.json.

The employee inputs the necessary data, the program converts it into an object and then a dictionary, and finally appends the new data to the employee-data.json.

Lastly, the program will call the do_again() function with 'write' as a parameter to activate the 'write' case.

---------- About search() ----------

The purpose of this function is to search an employee's information. 

I used the employee_search() and department_search() functions with the match-case.

Lastly, the program will call the do_again() function with 'search' as a parameter to activate the 'search' case.

---------- About employee_search() ----------

The purpose of this function is to support the search() function for helping the user to search for the employee's id or name

This returns a list, selected search and the user's search criteria.

---------- About department_search() ----------

The purpose of this function is to support the search() function for helping the user to search for the employee's department details (department name, manager, and phone_number). Since these details were incased in a dictionary, it required a different way of searching.

This returns a list, selected search and the user's search criteria.

---------- About update() ----------

The purpose of this function is to update a currently existing employee's department details (i.e. department name, manager, and phone number)

The update() will first take in the employee id criteria to search by employee id. Once input is received the program will display a list of employee ids that match the user's input and the user's input criteria. 

Next, the user will be asked to input the full id. This will enable to program to pull all the details associated to the id.

A function call will be made to update_details() where the user will address and confirm the details to be updated.

Lastly, the program will call the do_again() function with 'update' as a parameter to activate the 'update' case.

---------- About update_details() ----------

The purpose of this function is to gather the details necessary for updating information. 

The user will then be allowed to select which of the department details to change and also input the change they would like to make. They will also have to confirm whether they would like to make the change or not.

This is isolated from the update() function because it gives the user a chance to redo their detail information without having to re-type the entire id again.

---------- About update_now() ----------

The purpose of this function is to update the employee-data.json according to the id, update choice, and update change.