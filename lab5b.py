#!/usr/bin/env python3
#Author ID: Sohail Alakoozi

#lab5a - reading with 'r'
def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    s = open(file_name,'r') # So use open to read data.txt and return a file object. 
    read_data = s.read() # Store its contents into read_data string
    s.close()
    return read_data 


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    s = open(file_name,'r')
    read_data = s.read()
    s.close()
    return read_data.splitlines() # Use .splitlines() to properly split lines without keeping \n characters.
    



#lab5b - writing with 'w'
def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    s = open(file_name,'a') # 1) Opens the file in append mode.
    new_append = s.write(string_of_lines) # 2) s.write(argument) method adds string to the end of the file.
    s.close() # 3) File is closed
    return new_append


def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes each item from list to file where each item is one line
    s = open(file_name, 'w') # 1) Opens the file in overwrite mode or a new file is created.

    for item in list_of_lines: # 2) A loop to iterate over each line in the file.
        write_item = s.write(str(item) + '\n') # 3) write each item followed by a new line into the data object.

    s.close()
    return write_item
    
        
def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    s = open(file_name_read,'r') # Opens source file in read mode.

    f = open(file_name_write,'w')# Open destination file in write mode.

    line_number = 1 # This is used to keep track of the current line number as we iterate through the lines of the source file.

    for line in s: # Loop iterates through the lines of the source file. Each iteration gives one line from the file. 'line' represents the content of each line as the loop runs.
        
        f.write(f'{line_number}:{line}') # So now we write the formated output using a f-string with two placeholders. f-string allows us to easily insert values into the string.

        line_number += 1 # Used to increment the line_number by 1 after each line is written

    s.close()
    f.close()

        

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1)) # When ran 'seneca1.txt' is created.
    write_file_list(file2, list1)
    print(read_file_string(file2)) # When ran 'seneca2.txt' is created.
    copy_file_add_line_numbers(file2,file3)
    print(read_file_string(file3)) # When ran 'seneca3.txt' is created.

 