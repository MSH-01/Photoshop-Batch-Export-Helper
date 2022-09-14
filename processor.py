from util import *
from PhotoshopExportScript import menu
import csv
import numpy
import re

def smart_create_image_directories():
    try:
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
        
        #correct_directories = input("[ALERT] Does this template require " + directories_count + " number of folders? (Y/N)")

        for i in range(directories_count_int):
            os.mkdir(mypath+'/img'+str(i+1))
            print("[INFO] Image directories created.")
            menu()
    except:
        print("[ERROR] Image directories already exist.")
        menu()

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
