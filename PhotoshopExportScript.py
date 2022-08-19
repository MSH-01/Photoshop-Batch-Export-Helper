from os import listdir
from os.path import isfile, join
import xlsxwriter
import os
import shutil

# Get current path.
mypath = os.getcwd()
# Define image source directories.
image_source = [mypath+'/img1',mypath+'/img2',mypath+'/img3']
# Define output directory.
originals_dir = mypath+'/originals'


def create_spreadsheet():

    # Create lists of images.
    image1 = [f for f in os.listdir(image_source[0]) if os.path.isfile(join(image_source[0], f))]
    image2 = [f for f in os.listdir(image_source[1]) if os.path.isfile(join(image_source[1], f))]
    image3 = [f for f in os.listdir(image_source[2]) if os.path.isfile(join(image_source[2], f))]

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('variables.xlsx')
    worksheet = workbook.add_worksheet()
    # Write the top header cells.
    worksheet.write(0,0, "Image1")
    worksheet.write(0,1, "Image2")
    worksheet.write(0,2, "Image3")
    # Write image names for each row.
    for image in image1:
        worksheet.write_column(1,0,image1)
        worksheet.write_column(1,1,image2)
        worksheet.write_column(1,2,image3)
        print("[INFO] Row Created.")
    print("[INFO] Spreadsheet Created.")
    # Close the workbook.
    workbook.close()
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
