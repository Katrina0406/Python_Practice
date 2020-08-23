
# working with filesystem shell methods

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # copy over the permissions, modification times, and other info
        shutil.copy(src, dst) # this copies content
        shutil.copystat(src, dst) # this copies other info

        # rename the original file
        os.rename("textfile.txt", "newfile.txt")

        # put things into a ZIP archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == '__main__':
    main()