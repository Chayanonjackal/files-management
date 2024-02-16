import os
import shutil

# C:\Users\User\Downloads\test

def input_dir():
    dir = input('Input your directory...\n')
    # print(dir)
    return dir
    # return 'C:/Users/User/Downloads/test'

def move_file_to_folder(file_path, folder_path):
    try:
        shutil.move(file_path, folder_path)
        print(f"File '{file_path}' moved to '{folder_path}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_fiels(dir = input_dir()):
    try:
        files = os.listdir(dir)
        file_types = {}
        for file in files:
            name,extension = os.path.splitext(file)
            extension = extension[1:]
            file_types[extension] = file_types.get(extension, 0) + 1
            folder_path = dir+"/"+extension
            file_path = dir+"/"+file
        
            #create folder from file type
            try:
                os.mkdir(folder_path)
                print(f"Folder '{extension}' created successfully.")
                # put file inside folder
                move_file_to_folder(file_path,folder_path)

            except FileExistsError:
                print(f"Folder '{extension}' already exists.")
                # put file inside folder
                move_file_to_folder(file_path,folder_path)

            except Exception as e:
                print(f"An error occurred: {e}")

        print("all_files_type :",file_types)
    except FileNotFoundError:
        print(f"Directory '{dir}' not found.")


    

def main():
    list_fiels()

if __name__ == '__main__':
    main()
