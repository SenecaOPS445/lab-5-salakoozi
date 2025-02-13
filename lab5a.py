#!/usr/bin/env python3
# Author ID: Sohail Alakoozi

#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    s = open('data.txt','r') # So use open to read data.txt and return a file object. 
    read_data = s.read() # Store its contents into read_data string
    return read_data 


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    s = open(file_name,'r')
    read_data = s.read()
    return read_data.splitlines() # Use .splitlines() to properly split lines without keeping \n characters.
    

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))