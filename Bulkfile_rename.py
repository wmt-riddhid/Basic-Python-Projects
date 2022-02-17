# This is a bulk file re-name python project, in which program that can go into any folder on your computer and rename all of the files based on the conditions set in your Python code.

from importlib.resources import path
import os

def main():
    i = 0
    folder = "/home/wmt-riddhi/bulk_file"
    for filename in os.listdir(folder):
        my_dest = "img" + "i" + ".png"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
if __name__ == "__main__":
    main()