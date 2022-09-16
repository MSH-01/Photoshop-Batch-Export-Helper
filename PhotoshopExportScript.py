import processor
import util

def user_input(user_prompt):
    return input(user_prompt)
 
def menu():

    print("\nPS Batch Export Script")
    print("1) Create CSV \n2) Create Utility Directories \n3) Create Directories \n4) Smart Create Directories \n5) Reset Program \n6) Exit")
    user = input()
    try:
        if user == "1":
            processor.create_spreadsheet()
        elif user == "5":
            print("[ALERT] DOING THIS WILL DELETE ALL IMG FOLDERS AND THEIR CONTENTS!")
            reset_program = input("Are you sure you want to reset the program? (y/n): ")
            if reset_program.lower() == "y":
                util.reset_image_folders()
            else:
                print("[INFO] Reset Aborted.")
                menu()
        elif user == "2":
            util.create_utility_directories()
        elif user == "3":
            img_count = input("How many image folders do you want to create? ")
            util.create_image_directories(int(img_count))
        elif user == "4":
            processor.smart_create_image_directories()
        elif user == "6":
            print("[INFO] Program terminated.")
            exit()
        else:
            menu()

    except:
        print("[WARNING] Something went wrong.")
        menu()

menu()
