import os
import shutil
import csv
from os.path import isfile, join
import glob
import numpy

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

def create_image_directories(img_count):
    # Create directories for each image.
    try:
        for i in range(img_count):
            os.mkdir(mypath+'/img'+str(i+1))
        os.mkdir(mypath+'/psd')
        os.mkdir(mypath+'/temp')
        os.mkdir(mypath+'/output')
        print("[INFO] Image directories created.")
        print("[INFO] Utility directories created.")
        menu()
    except:
        print("[ERROR] Image directories already exist.")
        menu()

def menu():

    print("\nPS Batch Export Script")
    print("1)Create CSV \n2)Reset Program \n3)Create Directories \n4)Exit")
    user = input()
    try:
        if user == "1":
            create_spreadsheet()
        elif user == "2":
            print("[ALERT] DOING THIS WILL DELETE ALL IMG FOLDERS AND THEIR CONTENTS!")
            reset_program = input("Are you sure you want to reset the program? (y/n)")
            if reset_program == "y" or reset_program == "Y":
                reset_image_folders()
            else:
                print("[INFO] Reset Aborted.")
                menu()
        elif user == "3":
            img_count = input("How many image folders do you want to create? ")
            create_image_directories(int(img_count))
        elif user == "4":
            print("[INFO] Program terminated.")
            exit()

    except:
        print("[WARNING] Something went wrong.")
        menu()

menu()
