
import os
from string import digits
def rename_file():

    filenames = os.listdir(r"C:\Users\HP\Downloads\prank")
    print(filenames)


    os.chdir(r"C:\Users\HP\Downloads\prank")
    current_working_directory = os.getcwd()
    print(current_working_directory)


    for filename in filenames:
        os.rename(filename, filename.translate(str.maketrans('','',"0123456789")))
    newfilenames = os.listdir(r"C:\Users\HP\Downloads\prank")
    print(newfilenames)


rename_file()


#this is wonderful code




