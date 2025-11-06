'''Module for reading and writing employee data using pickle serialization.
'''
import pickle
import os

FILE_NAME = 'employees_db.dat'

def read_employees():
    '''Reads employee data from a binary file and returns a list of Employee objects.
    If the file does not exist, returns an empty list.
    '''
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'rb') as in_file:
        return pickle.load(in_file)

def write_employees(employees):
    '''Writes a list of Employee objects to a binary file.
    '''
    with open(FILE_NAME, 'wb') as out_file:
        pickle.dump(employees, out_file)
