#!/usr/bin/env python3
"""
Mass rename files 
"""

__author__ = "Mario Turco"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import os 
import argparse

def main():
    """ Main entry point of the script """
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', help="Path of the files to be renamed.", type= str, default='.')
    parser.add_argument('--extension', '-e', help="Extension of the files you want to rename. (* = everything)", type= str)
    parser.add_argument('--ignored_extensions', '-ie', help="Extension of the files you want to ignore.(Usage: '.py,.png')", type= str, default=[])
    args = parser.parse_args()
    path = args.path
    file_extension = args.extension
    ignored_extensions = args.ignored_extensions
    matching_file=0
    i=0
    total_number_of_files=0
    print(ignored_extensions)
    for files in os.listdir(path):
        if not files.startswith('.') and not extractExtension(files) in ignored_extensions:
            if extractExtension(files) == file_extension or file_extension=='*':
                extension = extractExtension(files)
                os.rename(files, str(i)+extension)
                i+=1
                matching_file+=1
            elif file_extension=='':
                os.rename(files, str(i))
                i+=1
                matching_file+=1
        total_number_of_files+=1
    print(str(matching_file)+  " files renamed out of " + str(total_number_of_files))

def extractExtension(file_name):
    ext = ""
    ext = '.'+(str(file_name).rsplit(sep="."))[-1]
    return ext;

if __name__ == "__main__":
    main()