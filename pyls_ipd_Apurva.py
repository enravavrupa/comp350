import os
import argparse
from typing import NamedTuple
from datetime import datetime

def main():
    options = get_command_line_args()
    list_files(options.dirname, options.longform, options.formatted)

class Options(NamedTuple):
    dirname: str
    longform: bool
    formatted: bool

# Options ==== tuple[str,bool,bool]

def get_command_line_args() -> Options:
    # ... argparse ...

    parser = argparse.ArgumentParser(prog="pyls", description="A baby version of ls.")

    # We now add descriptions for the expected arguments for our program.
    parser.add_argument(
        "dirname",
        nargs="?",  # Indicates that either 0 or one directory name can be given.
        default=".",  # Gives the default value to use when this argument is not given.
        # '.' means "current directory".
        help="The name of the directory whose contents are to be listed.",
    )
    parser.add_argument(
        "-l",
        "--longform",
        action="store_true",  # Indicates that the value is a boolean and no further
        # values need to be supplied on the command line.
        default=False,  # This is not really needed as False is the default already
        # when -l is not given on the command line. Including it
        # for illustration.
        help="Prints details about each file in the format -\n"
        "<timestamp> <filesize> <filename>",
    )
    parser.add_argument(
        "-F",
        "--formatted",
        action="store_true",
        default=False,
        help="Adds a character to tell you whether its a file or a directory.",
    )

    # Now we ask argparse to use the above information to interpret the
    # arguments and give us an object which will have `.dirname`,
    # `.longform` and `/.formatted` attributes we can access instead of
    # having to check for all the combinations ourselves.
    # Furthermore, if you call your program with either the `-h` or `--help``
    # flag, it will print out all of the specification above in a nice format
    # as help. This is a convention employed by most command line programs.
    args = parser.parse_args()

    return Options(args.dirname, args.longform, args.formatted)

class FileInfo(NamedTuple):
    name: str
    modtime: datetime
    size: int
    isdir: bool

def list_files(dirname: str, longform: bool, formatted: bool) -> None:
    """
    This function has been modified to sort via size in descending order
    
    Having the IPD structure makes it much easier to access the size of the
    files than it was for the original pyls prograrm
   
    Example:
    list_file("a", True, True) -> [(i, 12:05:00, 7800, /), (j, 12:05:00, 78, *), (k, 12:05:00, 7, *)]
    """
    validate_dir(dirname)
    contents : list[FileInfo] = sorted(find_contents_of_directory(dirname), key = FileInfo.size, reverse = True)
    presentation : list[str] = [present_file(fileinfo, longform, formatted) for fileinfo in contents]
    print_strings(presentation)

def validate_dir(dirname: str) -> bool:
    if os.path.isdir(dirname):
        return True
    raise Exception("Invalid directory " + dirname)

def find_contents_of_directory(dirname: str) -> list[FileInfo]:
    filenames = os.listdir(dirname)
    return [get_fileinfo(dirname, filename) for filename in filenames]

def get_fileinfo(dirname: str, filename: str) -> FileInfo:
    path = os.path.join(dirname, filename)
    isdir = os.path.isdir(path)
    stat = os.stat(path)
    modtime = stat.st_mtime
    size = stat.st_size
    return FileInfo(filename, datetime.fromtimestamp(modtime), size, isdir)

def present_file(fileinfo : FileInfo, longform: bool, formatted: bool) -> str:
    formatchar = '/' if fileinfo.isdir else ''
    if longform:
        if formatted:
            return f"{fileinfo.modtime.isoformat()} {fileinfo.size} {fileinfo.name}{formatchar}"
        else:
            return f"{fileinfo.modtime.isoformat()} {fileinfo.size} {fileinfo.name}"
    else:
        if formatted:
            return f"{fileinfo.name}{formatchar}"
        else:
            return fileinfo.name


def print_strings(lines: list[str]) -> None:
    for s in lines:
        print(s)

if __name__ == "__main__":
    main()
