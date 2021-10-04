from os import listdir
from os.path import isfile, join
import xlsxwriter
import os
import glob
import shutil

image_source = ['C:/Users/moham/Desktop/PhotoExports/img1','C:/Users/moham/Desktop/PhotoExports/img2','C:/Users/moham/Desktop/PhotoExports/img3']
originals_dir = 'C:/Users/moham/Desktop/PhotoExports/originals'

def create_spreadsheet():
    mypath = os.getcwd()

    image1 = [f for f in os.listdir(mypath+"\img1") if os.path.isfile(join(mypath+"\img1", f))]
    image2 = [f for f in os.listdir(mypath+"\img2") if os.path.isfile(join(mypath+"\img2", f))]
    image3 = [f for f in os.listdir(mypath+"\img3") if os.path.isfile(join(mypath+"\img3", f))]

    workbook = xlsxwriter.Workbook('variables.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0,0, "Image1")
    worksheet.write(0,1, "Image2")
    worksheet.write(0,2, "Image3")
    for image in image1:
        worksheet.write_column(1,0,image1)
        worksheet.write_column(1,1,image2)
        worksheet.write_column(1,2,image3)
    workbook.close()
    menu()


def delete_old_files():
    folders = ['C:/Users/moham/Desktop/PhotoExports/output','C:/Users/moham/Desktop/PhotoExports/originals','C:/Users/moham/Desktop/PhotoExports/img1','C:/Users/moham/Desktop/PhotoExports/img2','C:/Users/moham/Desktop/PhotoExports/img3']
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
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
    print("1)Create spreadsheet \n2)Copy images to original \n3)Delete old image files")
    user = input()
    try:
        if user == "1":
            create_spreadsheet()
        elif user == "2":
            for source in image_source:
                copytree(source, originals_dir)
        elif user == "3":
            delete_old_files()
    except:
        print("something went wrong")
        menu()

menu()
