import os
import shutil
import csv
from os.path import isfile, join
import glob

# Get current path.
mypath = os.getcwd()

def create_spreadsheet():
    # Defines a list for each image folder and populates it with paths of images.
    image1 = [f for f in os.listdir(image_source[0]) if os.path.isfile(join(image_source[0], f))]
    image2 = [f for f in os.listdir(image_source[1]) if os.path.isfile(join(image_source[1], f))]
    image3 = [f for f in os.listdir(image_source[2]) if os.path.isfile(join(image_source[2], f))]

    # Needs to be updated to make as many columns as are image folders.
    header = ["Image1","Image2","Image3"]

    # Defines list of image folders   
    images = [image1,image2,image3]


    # Gets rid of any non .jpg files (!!!REPLACE THIS!!!)
    for image_list in images:
        for image in image_list:
            if image.endswith(".DS_Store") or image.endswith(".txt"):
                image_list.remove(image)
                print("[ALERT] "+image+" removed.")
                break
                
    # Writes CSV
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


    # Make list of all directories.
    reset_program = input("Are you sure you want to reset the program? (y/n)")
    if reset_program == "y" or reset_program == "Y":
        folders = [mypath+'/output',mypath+'/img1',mypath+'/img2',mypath+'/img3',mypath+'/psd']
        # Go through each directory.
        for folder in folders:
            # Go through files in each directory.
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        print("[ALERT] "+file_path+" deleted.")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        print("[ALERT] "+file_path+" deleted.")
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            print("[ALERT] Files at "+ folder +" deleted.")
        try:
            os.remove('variables.csv')
            print("[ALERT] CSV deleted.")
        except:
            print("[ALERT] CSV not found / already deleted")
        print("[INFO] Program reset.")
        menu()
    else:
        print("[INFO] Reset Aborted.")
        menu()

def reset_image_folders():
    # Make list of all image directories.
    image_folders = glob.glob('img*')
    for item in image_folders:
        if os.path.isdir(item):
            shutil.rmtree(item)
            print("[ALERT] /"+item+" deleted.")

        else:
            print("[ALERT] /"+item+" not found.")
    print("[INFO] Image folders reset.")
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
        print("[INFO] Image directories created.")
        menu()
    except:
        print("[ALERT] Image directories already exist.")
        menu()

def menu():

    print("\nPS Batch Export Script")
    print("1)Create CSV \n2)Reset Program \n4)Create Directories \n3)Exit")
    user = input()
    try:
        if user == "1":
            create_spreadsheet_new()
        elif user == "2":
            print("[ALERT] DOING THIS WILL DELETE ALL IMG FOLDERS AND THEIR CONTENTS!")
            reset_program = input("Are you sure you want to reset the program? (y/n)")
            if reset_program == "y" or reset_program == "Y":
                reset_image_folders()
            else:
                print("[INFO] Reset Aborted.")
                menu()
        elif user == "3":
            print("[INFO] Program terminated.")
            exit()
        elif user == "4":
            img_count = input("How many image folders do you want to create? ")
            create_image_directories(int(img_count))
    except:
        print("[WARNING] Something went wrong.")
        menu()


def create_spreadsheet_new():
    folders = img_folder_list()
    folders.sort()
    images = []
    header = []
    count = 0
    for folder in folders:
        images.append([f for f in os.listdir(mypath+'/'+folder) if os.path.isfile(join(mypath+'/'+folder, f))])
    
    for i in range(img_folder_count()):
        header.append("Image"+str(i+1))

    # Gets rid of any non .jpg files (!!!REPLACE THIS!!!)
    for image_list in images:
        for image in image_list:
            if image.endswith(".jpg") or image.endswith(".png"):
                print("[ALERT] "+image+" skipped.")
            else:
                image_list.remove(image)
                print("[ALERT] "+image+" removed.")


    print("[INFO] Spreadsheet Created.")
    menu()


menu()
