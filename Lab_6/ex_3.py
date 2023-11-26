"""

    ! the script takes 1 argument, the path to a folder;

    calculates the total size of all files in a directory provided as a command line argument.

"""


import sys
import os
from ex_1 import folder_exists


def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return None

    folder_path = sys.argv[1]

    if folder_exists(folder_path):
        total_size = 0
        exists_files = False
        for (root, directories, files) in os.walk(folder_path):
            for fileName in files:
                full_file_name = os.path.join(root, fileName)
                try:
                    size_curr_file = os.path.getsize(full_file_name)
                    exists_files = True
                    total_size += size_curr_file
                    # print(f"File {full_file_name} has size {size_curr_file} bytes")
                except OSError as e:
                    print(f"Exception : {e} at file {full_file_name}")

        if not exists_files:
            print("No files in folder")
        else:
            print(f"Total size of all files in folder {folder_path} is {total_size} bytes")
    else:
        return None


if __name__ == "__main__":
    main()
