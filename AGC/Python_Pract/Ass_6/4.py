"""
Create a function showEmployee() in such a way that it should accept employee name,
and it’s salary and display both, and if the salary is missing in function call it should
show it as 9000
"""
def showEmployee(emp_name,salary=9000):
    print('The Employee name is := ',emp_name);
    print('The Employee salary is := ',salary);


emp_name=str(input('\nEnter the employee name\n'))
salary=int(input('\nEnter the salary\n'))
showEmployee(emp_name,salary)
showEmployee(emp_name)