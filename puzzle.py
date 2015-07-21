import string
import os
def rename_files():
    from string import maketrans
    insub = "aeiou"
    outsub = "12345"
    theboy = maketrans(insub,outsub)

    file_list = os.listdir(r"C:\Users\Feedah\Desktop\Python Stuff\Programming Foundations with Python Videos\alphabet\alphabet")

    working_dir = os.getcwd()
    print("you are currently working in "+ working_dir)
    os.chdir(r"C:\Users\Feedah\Desktop\Python Stuff\Programming Foundations with Python Videos\alphabet\alphabet")
    for each_name in file_list:
        os.rename(each_name, each_name.translate(theboy))
    os.chdir(working_dir)
    print (file_list)
rename_files()
