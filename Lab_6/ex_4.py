"""

    ! the script takes 1 argument, the path to a folder;

    counts the number of files with each extension in a given directory.

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

        files_extensions = {}

        for files in os.listdir(folder_path):
            file_path = os.path.join(folder_path, files)
            if os.path.isfile(file_path):
                extension = os.path.splitext(file_path)[1]

                if extension in files_extensions:
                    files_extensions[extension] += 1
                else:
                    files_extensions[extension] = 1

        if len(files_extensions) == 0:
            print("No files in folder")
        else:
            print("Number of files with each extension :")
            for extension, count in files_extensions.items():
                print(f"{extension} : {count}")

    else:
        return None


if __name__ == "__main__":
    main()
