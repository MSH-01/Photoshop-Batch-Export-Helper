from os import listdir
from os.path import isfile, join
import xlsxwriter
import os
import glob
import shutil

mypath = os.getcwd()
image_source = [mypath+'/img1',mypath+'/img2',mypath+'/img3']
originals_dir = mypath+'/originals'


def create_spreadsheet():

    image1 = [f for f in os.listdir(image_source[0]) if os.path.isfile(join(image_source[0], f))]
    image2 = [f for f in os.listdir(image_source[1]) if os.path.isfile(join(image_source[1], f))]
    image3 = [f for f in os.listdir(image_source[2]) if os.path.isfile(join(image_source[2], f))]

    workbook = xlsxwriter.Workbook('variables.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0,0, "Image1")
    worksheet.write(0,1, "Image2")
    worksheet.write(0,2, "Image3")
    for image in image1:
        worksheet.write_column(1,0,image1)
        worksheet.write_column(1,1,image2)
        worksheet.write_column(1,2,image3)
        print("[INFO] Row Created.")
    print("[INFO] Spreadsheet Created.")
    workbook.close()
    menu()


def reset():
    folders = [mypath+'/output',mypath+'/originals',mypath+'/img1',mypath+'/img2',mypath+'/img3']
    for folder in folders:
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
        print("[INFO] "+ folder +" deleted.")
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
    print("1)Create spreadsheet \n2)Copy images to original \n3)Reset Program")
    user = input()
    try:
        if user == "1":
            create_spreadsheet()
        elif user == "2":
            for source in image_source:
                copytree(source, originals_dir)
        elif user == "3":
            reset()
    except:
        print("something went wrong")
        menu()

menu()
