'''
As a GCP Architect, you need to organize log file names from different virtual machines (VMs) 
in Google Compute Engine.

Each VM generates a log file, and you need to store the log file names in variables, 
format them properly, and perform basic operations on them.

Task:
Define three variables to store log file names for:

A web server
A database server
An application server
Use proper naming conventions:

Use camelCase for the web server log variable.
Use snake_case for the database server log variable.
Use PascalCase for the application server log variable.
Perform the following operations:

Print each log file name.
Get and print the first character of the database log file name (treat it as an array).
Create an empty log file using touch (Linux command).
Copy the web server log file to a backup file using cp.
Display the last 5 commands used in the terminal using history.
'''

Web_server = 'Web_server.log'
result = 'Web_server'
print('Define log file name: ', Web_server)

DataBase = 'DataBase.log'
result = 'DataBase'
print('Define log file name:', DataBase)

application_server = 'application_server.log'
result = 'application_server'
print('Define log file name:', application_server)
print()

Welcome = 'Database Log File'

Database_log_file = [DataBase]
output = DataBase[0]
print(output)

Database_log_file = [Web_server]
output = Web_server[0]
print(output)

Database_log_file = [application_server]
output = application_server[0]
print(output)

