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
            if image.endswith(".DS_Store"):
                image1.remove(image)
                image2.remove(image)
                image3.remove(image)
            else:
                writer.writerow(["img1/"+image1[counter],"img2/"+image2[counter],"img3/"+image3[counter]])
                counter+=1
                print("[INFO] Row Created.")
    print("[INFO] Spreadsheet Created.")
    menu()



def reset():
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
        delete_csv()
        print("[INFO] Program reset.")
        menu()
    else:
        print("[INFO] Reset Aborted.")
        menu()

def delete_csv():
    os.remove('variables.csv')
    print("[INFO] CSV deleted.")
    menu()


def menu():
    print("\nPS Batch Export Script")
    print("1)Create CSV \n2)Reset Program \n3)Exit")
    user = input()
    try:
        if user == "1":
            create_spreadsheet()
        elif user == "2":
            reset()
        elif user == "3":
            print("[INFO] Program terminated.")
            exit()
    except:
        print("[WARNING] Something went wrong.")
        menu()

menu()
