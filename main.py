import  os
import shutil
import time

target_folder = input("enter the folder path : ")

def get_file_type(file):
    name_list = file.split(".")
    name_list_len = len(name_list)
    file_type = name_list[name_list_len - 1]
    return  file_type

def get_files_types():
    files = os.listdir(target_folder)
    all_types = []
    for file in files:
        file_type = get_file_type(file)
        if not all_types.count(file_type):
            all_types.append(file_type)
    return all_types

def create_types_folders(files_types):
    for file_type in files_types:
        try:
            os.mkdir(target_folder + "\\" + file_type)
        except:
            pass


def sort_files():
    os.chdir(target_folder)
    downloaded_files = os.listdir()
    sorting_folder =  os.listdir(target_folder)

    for file in downloaded_files :
        file_type = get_file_type(file)
        if(len(file_type) > 10) :
            continue
        if file_type in sorting_folder :
            shutil.move(f"{target_folder}\\{file}",f"{target_folder}\\{file_type}")


while (True) :

    files_types = get_files_types()
    create_types_folders(files_types)
    sort_files()
    time.sleep(5000)