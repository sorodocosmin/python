

"""
    ! the script takes 1 argument, the path to a folder;

rename all the files in a folder with following format
<file_name> -> file{index}_<filename>
ex: a.txt -> file1_a.txt
Note : all files will be ranamed, so if we firstly try to rename a.txt to file1_a.txt
and file1_a.txt already exists, it will be saved in a list,
and after we rename file1_a.txt in file_{index}_file1_a.txt
we will get back to a.txt and rename it
"""

import os
import sys
from ex_1 import folder_exists


def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return None

    folder_path = sys.argv[1]

    if folder_exists(folder_path):
        counter = 1
        exists_files = False
        list_new_name_already_exists = []
        for files in os.listdir(folder_path):
            file_path = os.path.join(folder_path, files)
            if os.path.isfile(file_path):
                exists_files = True
                new_file_name = os.path.join(folder_path, f"file{counter}_{files}")
                counter += 1
                try:
                    os.rename(file_path, new_file_name)
                except FileExistsError:
                    list_new_name_already_exists.append((file_path, new_file_name))
                except PermissionError as e:
                    print(f"Permission denied for file {file_path} -- cannot rename it : {e}")
                    counter -= 1
                except Exception as e:
                    print(f"Exception : {e} at file {file_path}")
                    counter -= 1

        if not exists_files:
            print("No files in folder")

        for file_path, new_file_path in list_new_name_already_exists:
            try:
                os.rename(file_path, new_file_path)
            except PermissionError as e:
                print(f"Permission denied for file {file_path} -- cannot rename it : {e}")
            except Exception as e:
                print(f"Exception : {e} at file {file_path}")

    else:
        return None


if __name__ == '__main__':
    main()
