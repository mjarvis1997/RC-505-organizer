# 
# see readme here for details on usage
#



import os
import sys
from os.path import exists

# name of new root folder
root = "505-organized"

# if root folder already exists
if(exists(root)):
   print("ERROR: Folder named '505-organized' already exists, exiting program to avoid overwriting any existing files\nDelete or move the existing 505-organized folder and then run again")
   sys.exit()

# create root folder
os.mkdir(root)

# function to move files from individual folders into new aggregate numbered folder
def moveSong(songNumber):

    # name of new song folder
    songFolder = root + "/" + str(songNumber)

    # create new folder for song
    os.mkdir(songFolder)

    # for each track in the current song
    for i in range(1,6):

        # construct file paths
        currFolderPath = str(songNumber).zfill(3) + "_" + str(i)
        currFilePath = currFolderPath + "/" + currFolderPath + ".WAV"
        newFolderPath = root + "/" + str(songNumber)
        newFilePath = newFolderPath + "/" + str(songNumber) + "_"+ str(i) + ".WAV"

        # if file exists in folder for the current track
        if os.listdir(currFolderPath):

            # move file to new folder
            os.rename(currFilePath, newFilePath)

            print(str("old: " + currFolderPath + " | new: " +  newFolderPath))
            print(str("old: " + currFilePath + " | new: " +  newFilePath))

# for each song in the 505's folders
for i in range(1,11):

    # for each track in the current song
    for ii in range(1,6):

        folderName = str(i).zfill(3) + "_" + str(ii)

        # if there are not files in the current folder
        if not os.listdir(folderName):
            continue

        # if any of the songs folders have files
        
        moveSong(i)
        break
