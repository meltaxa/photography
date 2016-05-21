#!/usr/bin/env python

import os
from os.path import expanduser
import glob
import time
import datetime
import shutil
import platform

if platform.system() == "Windows":
    source="E:/"
else:
    source="/Volumes/NO NAME"

home=expanduser("~")
target=home+"/Pictures"

# Only copy files with these extensions
photo_ext=[".ARW",".JPG",".PNG",".GIF",".ORF"]

# Create a directory is it doesn't exist
def makedir(destination):
    if not os.path.exists(destination):
        print "[INFO] Creating directory %s" % destination
        os.makedirs(destination)

# Create a date based directory structure
def create_target_dir(todays_date):
    folder=todays_date.split('/')
    year=folder[0]
    makedir(target + "/" + year)
    photo_folder=glob.glob(target + "/" + year + "/" + todays_date.replace('/','-') + "*")
    if photo_folder:
        if len(photo_folder) > 1:
            use_folder=target + "/" + year + "/" + todays_date.replace('/','-') + " latest"
            makedir(use_folder)
        else:
            use_folder=photo_folder[0]
    else:
        use_folder=target + "/" + year + "/" + todays_date.replace('/','-')
        makedir(use_folder)
    return use_folder

# Traverse thru the SD card and fetch the photos
for root, dirs, files in os.walk(source):
    for f in files:
        filename, file_extension = os.path.splitext(f)
        if file_extension.upper() in map(str.upper, photo_ext):
            t=os.path.getmtime(root+"/"+f)
            d=datetime.datetime.fromtimestamp(t)
            response=create_target_dir(d.strftime('%Y')+"/"+d.strftime('%m')+"/"+d.strftime('%d'))
            if not os.path.isfile(response+"/"+f):
                shutil.copy2(root+"/"+f,response+"/"+f)
                print "copying %s to %s" % (f,response+"/"+f)
