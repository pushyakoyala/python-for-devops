import os

def list_files_in_folderpath(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "files not found"
    except PermissionError:
        return  None, "do Not Have Access"
    
def main():
    folder_paths = input('ENTER THE FOLDER NAME WITH SPACES :').split()

    for folder_path in folder_paths:
        files, error_message = list_files_in_folderpath(folder_path)
        if files:
            print("files in " + folder_path)
            for file in files:
                print(file)
        else:
            print((folder_path)+ ' ' + error_message)

main()



        

    