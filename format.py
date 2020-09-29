#!/usr/bin/env python3
import argparse
import sys
import os.path
file_location = None
default_character_length = 80
def parse_file():
    f = open(file_location, "r+")
    text = f.read()
    array_read = text.split("\n")
    #truncate the entire file to empty it 
    f.truncate()
    write_array = []
    for element in array_read:
        if len(element) <= default_character_length:
            write_array.append(element)
        else:
            i = 0
            while i+80 <= len(element)-1:
                temp = i+80
                while element[temp] != " ":
                    temp-=1
                write_array.append(element[i: temp])
                i = temp+1
            if i < len(element)-1:
                write_array.append(element[i: len(element)])
    f.write("\n".join(write_array))
parser = argparse.ArgumentParser()
parser.add_argument("-location", dest = 'location', type = str, help  = "enter the path of the file from the location of this python file make sure it's a txt file")
parser.add_argument("--characters", dest = 'characters', type = int, default = 80, help = "enter the number of characters per lne default will be set to 80")
args = parser.parse_args()
file_location = args.location
default_character_length = args.characters
if file_location == None:
    print("enter an argument type -h at the end for help")
    sys.exit()
if file_location[len(file_location)-4: len(file_location)] != ".txt":
    print("please enter a txt file")
    sys.exit()
if not os.path.isfile(file_location):
    print("enter a valid file")
    sys.exit()
else:
    parse_file()
