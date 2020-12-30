# main/py

# Third party imports
# pathlib for handling paths
import pathlib

# sys for receiving args 
import sys

def read_data(file_path) -> :
    # Extracts the file extention and stores it into format
    # The dot is removed as well
    format = file_path.suffix.lstrip('.')
    data = ''
    # Read content of txt files
    if format == ‘txt’:
        with open (file_path,'r') as _file:
            data = _file.read()
    return data

def main(file_path:str) -> str:
    # Create a Path based on the file_path str
    file_path = pathlib.Path(file_path)
    # Read file data and stores into data
    data = read_data(file_path)
    return data

# This will be trigger when the main.py is executed as main
if __name__ == '__main__':
    # Set a default result to avoid errors
    result = "File path should be provided as argument: main.py 'file_path'"
    # argv[0] is the name of the running file, main.py in this case
    if len(sys.argv) > 1:
        # Call our main with the first argument sent by CLI
        result = main(sys.argv[1])
    print (result)