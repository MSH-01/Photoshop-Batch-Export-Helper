from itertools import count
from os import listdir
from os.path import isfile, join
import os
import shutil
import csv

# Get current path.
mypath = os.getcwd()
# Define image source directories.
image_source = [mypath+'/img1',mypath+'/img2',mypath+'/img3']
# Define output directory.
originals_dir = mypath+'/originals'


def create_spreadsheet():
    image1 = [f for f in os.listdir(image_source[0]) if os.path.isfile(join(image_source[0], f))]
    image2 = [f for f in os.listdir(image_source[1]) if os.path.isfile(join(image_source[1], f))]
    image3 = [f for f in os.listdir(image_source[2]) if os.path.isfile(join(image_source[2], f))]
    header = ["Image1","Image2","Image3"]

    with open('variables.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        counter = 0
        for image in image1:
            writer.writerow(["img1/"+image1[counter],"img2/"+image2[counter],"img3/"+image3[counter]])
            counter+=1
            print("[INFO] Row Created.")
    print("[INFO] Spreadsheet Created.")
    menu()



def reset():
    # Make list of all directories.
    reset_program = input("Are you sure you want to reset the program? (y/n)")
    if reset_program == "y" or reset_program == "Y":
        folders = [mypath+'/output',mypath+'/originals',mypath+'/img1',mypath+'/img2',mypath+'/img3']
        # Go through each directory.
        for folder in folders:
            # Go through files in each directory.
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        print("[INFO] "+file_path+" deleted.")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print("[INFO] "+file_path+" deleted.")
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            print("[INFO] Files at "+ folder +" deleted.")
        print("[INFO] Program reset.")
        menu()
    else:
        print("[INFO] Reset Aborted.")
        menu()


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
    menu()


def menu():
    print("PS Batch Export Script")
    print("1)Create spreadsheet \n2)Copy images to original \n3)Reset Program \n4)Exit")
    user = input()
    try:
        if user == "1":
            create_spreadsheet()
        elif user == "2":
            for source in image_source:
                copytree(source, originals_dir)
        elif user == "3":
            reset()
        elif user == "4":
            print("[INFO] Program terminated.")
            exit()
    except:
        print("something went wrong")
        menu()

menu()
