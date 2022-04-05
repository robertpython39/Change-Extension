#-------------------------------------------------------------------------------
# Name:        Change extensions
# Purpose:     Work
#
# Author:      nicolescu
#
# Created:     03/04/2022
# Copyright:   (c) nicol 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import os
import sys


folder_path = input(r'Enter folder path (Copy-Paste):')
input_extension = input("Enter file input extension( Ex: .html, .xls etc):")
output_extension = input("Enter file output extension( Ex: .html, .xls etc):")

folder = folder_path
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace(input_extension, output_extension)
    output = os.rename(infilename, newname)

exit_output = input("Press any key to exit...")

