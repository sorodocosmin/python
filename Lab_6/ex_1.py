
"""
    ! this script should be run with exactly 3 arguments
    1. script name
    2. path to directory
    3. extension

it assumes that an extension can only be formed by letters and numbers
it assumes that an extension should start with dot

it will print the content of the files from the given directory, with the given extension
in the following format:
------------------------------------
File <full_path_to_file>
Content:
<file_content>
------------------------------------
"""
import sys
import os


def main():

    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return None

    folder_path = sys.argv[1]
    extension = sys.argv[2]

    if folder_exists(folder_path) and is_valid_extension(extension):
        # go recursively through all files in folder
        for (root, directories, files) in os.walk(folder_path):
            for fileName in files:
                full_file_name = os.path.join(root, fileName)
                if os.path.splitext(fileName)[1] == extension:
                    # it might be a good idea to print only a part of the content (first n characters)
                    # for some really big files, it might take a while to print the whole content and also,
                    # won t be able to see the previous files content
                    content = get_content_file(full_file_name)
                    if content is not None:
                        print("------------------------------------")
                        print(f"File {full_file_name}")
                        print(f"Content:\n{content}")
                        print("------------------------------------")
    else:
        return None


def get_content_file(path_to_file):
    try:
        # !!!
        # idk why, but even if the file is not readable, the function os.access(path_to_file, os.R_OK) will return True ... ??
        if not os.access(path_to_file, os.R_OK):
            raise InvalidAccessRights("File is not readable")
        # I tried with os.stat --> same result (not working)

        with open(path_to_file, "r") as file:
            return file.read()

    except InvalidAccessRights as e:
        print("Invalid access rights : ", e)
    except PermissionError as permission_error:  # this will catch if the file cannot be read
        print("Permission exception : ", permission_error)
        return None
    except Exception as e:
        print(path_to_file)
        print("Exception: ", e)


def folder_exists(folder_path):

    try:
        if not os.path.exists(folder_path):
            raise DirectorDoesNotExist("Directory does not exist")

    except DirectorDoesNotExist as e:
        print("Exception: ", e)
        return False

    return True


def is_valid_extension(extension):

    try:
        if len(extension) < 2:
            raise InvalidExtensionNaming("Extension should be at least 2 characters long")
        elif not extension.startswith("."):
            raise InvalidExtensionNaming("Extension should start with dot")
        elif not extension[1:].isalnum():
            raise InvalidExtensionNaming("Extension should contain only letters and numbers")

    except InvalidExtensionNaming as e:
        print("Exception: ", e)
        return False

    return True


class InvalidExtensionNaming(BaseException):
    pass


class DirectorDoesNotExist(BaseException):
    pass


class InvalidAccessRights(BaseException):
    pass


if __name__ == "__main__":
    main()
