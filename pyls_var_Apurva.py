# Imports make the mentioned "modules" accessible to the code within
# this file, which is itself a "module".
import argparse
import os


def main() -> None:
    parser = argparse.ArgumentParser(prog="find_files_using_pyls", description="A version of pyls that enumerates the different kinds of files")

    # Now we ask argparse to use the above information to interpret the
    # arguments and give us an object which will have `.dirname`,
    # `.longform` and `/.formatted` attributes we can access instead of
    # having to check for all the combinations ourselves.
    # Furthermore, if you call your program with either the `-h` or `--help``
    # flag, it will print out all of the specification above in a nice format
    # as help. This is a convention employed by most command line programs.
    args = parser.parse_args()

#print(os.listdir("/home/avrupaenrav"))
os.chdir("/home")

def find_files_using_pyls(dirname: str, file: bool) -> None:
    """
    DATA REPRESENTATION
    -------------------

    In this case, we're choosing a **representation** where we represent
    the directory name to list as a string and the choice of longform and
    formatted output as two boolean values.
   
    SIGNATURE 
    ---------
    The "signature" of the procedure below can be written as
              str -> None

    PURPOSE
    -------

    - :param dirname: This parameter supplies the function with the name of the directory to be scanned.
    
    EXAMPLE
    _______
    
    find_files_using_pyls("a", True) -> "File: 50, File Size: 5600, Directories: 10, Directories Size: 9908, Links: 5, Link Size: 765, DevDrives: 2, DevDrive Size: 785, Others: 23, Other Size: 8700"

    """
    # Replace the "pass" below with your implementation.
    file = 0
    direct = 0
    link = 0
    devdrive = 0
    other = 0
    file_size = 0
    direct_size =0
    link_size = 0
    devdrive_size = 0
    other_size = 0
    dirpath = os.path.join("/home", dirname)
    lst = os.listdir(dirpath)
    for i in lst:
        j = os.path.join(dirpath, i)
        if os.path.isfile(j):
            counter(file)
            file_size  += os.path.getsize(j)
        elif os.path.isdir(j):
            counter(direct)
            direct_size += os.path.getsize(j)
        elif os.path.link(j):
            counter(link)
            link_size += os.path.getsize(j)
        elif os.path.devdrive(j):
            counter(devdrive)
            devdrive_size += os.path.getsize(j)
        else:
            counter(other)
            other_size += os.path.getsize(j)
    return f"File: {file}, File Size: {file_size}, Directories: {direct}, Directories Size: {direct_size}, Links: {link}, Link Size: {link_size}, DevDrives: {devdrive}, DevDrive Size: {devdrive_size}, Others: {other}, Other Size: {other_size}"

def counter(i: int) -> int:
    """
    increments the count of the given interger variable by 1
    """
    i = i + 1
    return i

find_files_using_pyls("avrupaenrav")

if __name__ == "__main__":
    main()
