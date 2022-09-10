import os
import shutil
import csv
from os.path import isfile, join
import glob
import numpy
import re

# Get current path.
mypath = os.getcwd()

def create_spreadsheet():
    folders = img_folder_list()
    folders.sort()
    folder_list = []
    header = []
    for folder in folders:
        folder_list.append([folder+"/"+f for f in os.listdir(mypath+'/'+folder) if f.endswith(".jpg") or f.endswith(".jpeg")])
    
    for i in range(img_folder_count()):
        header.append("Image"+str(i+1))
    
    transposed_list = numpy.transpose(folder_list)

    #this works but is hardcoded solution
    with open('variables.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in transposed_list:
            writer.writerow(row)
            print("[ALERT] Row Created.")

    print("[INFO] Spreadsheet Created.")

    menu()

def reset_image_folders():
    # Make list of all image directories.
    reset_folders = glob.glob('img*') + glob.glob('output') + glob.glob('temp') + glob.glob('psd')
    for item in reset_folders:
        if os.path.isdir(item):
            shutil.rmtree(item)
            print("[ALERT] /"+item+" deleted.")

        else:
            print("[ALERT] /"+item+" not found.")
    print("[INFO] All folders reset.")
    menu()

def img_folder_count():
    # Counts number of image folders.
    return len(img_folder_list())

def img_folder_list():
    return glob.glob('img*')

def find_psd_files():
    return glob.glob('templates/*.psd')

def user_input(user_prompt):
    return input(user_prompt)


def smart_create_image_directories():
    print("\nSmart Create Directories")
    template_dictionary = {}
    for count, template in enumerate(find_psd_files()):
        print(str(count+1)+") "+ template.replace('templates/',''))
        template_dictionary[str(count+1)] = template.replace('templates/','')

    template_choice = str(user_input("Please select a template: "))

    directories_count = re.findall("\d",template_dictionary[template_choice])
    directories_count_int = 0
    for number in directories_count:
        directories_count_int+= int(number)
    
    for i in range(directories_count_int):
        os.mkdir(mypath+'/img'+str(i+1))
        print("[INFO] Image directories created.")
    menu()

def create_utility_directories():
    try:
        os.mkdir(mypath+'/psd')
        os.mkdir(mypath+'/temp')
        os.mkdir(mypath+'/output')
        print("[INFO] Utility directories created.")
        menu()
    except:
        print("[ERROR] Utility directories already exist.")
        menu()

def create_image_directories(img_count):
    # Create directories for each image.
    try:
        for i in range(img_count):
            os.mkdir(mypath+'/img'+str(i+1))
        print("[INFO] Image directories created.")
        menu()
    except:
        print("[ERROR] Image directories already exist.")
        menu()

def menu():

    print("\nPS Batch Export Script")
    print("1) Create CSV \n2) Create Utility Directories \n3) Create Directories \n4) Smart Create Directories \n5) Reset Program \n6) Exit")
    user = input()
    try:
        if user == "1":
            create_spreadsheet()
        elif user == "5":
            print("[ALERT] DOING THIS WILL DELETE ALL IMG FOLDERS AND THEIR CONTENTS!")
            reset_program = input("Are you sure you want to reset the program? (y/n)")
            if reset_program == "y" or reset_program == "Y":
                reset_image_folders()
            else:
                print("[INFO] Reset Aborted.")
                menu()
        elif user == "2":
            create_utility_directories()
        elif user == "3":
            img_count = input("How many image folders do you want to create? ")
            create_image_directories(int(img_count))
        elif user == "4":
            smart_create_image_directories()
        elif user == "5":
            print("[INFO] Program terminated.")
            exit()

    except:
        print("[WARNING] Something went wrong.")
        menu()

menu()
