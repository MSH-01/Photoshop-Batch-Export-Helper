import glob
import os
import shutil
import PhotoshopExportScript

mypath = os.getcwd()

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
        PhotoshopExportScript.menu()
    except:
        print("[ERROR] Image directories already exist.")
        PhotoshopExportScript.menu()

def find_psd_files():
    return glob.glob('templates/*.psd')

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
    PhotoshopExportScript.menu()

def img_folder_count():
    # Counts number of image folders.
    return len(img_folder_list())

def img_folder_list():
    return glob.glob('img*')
