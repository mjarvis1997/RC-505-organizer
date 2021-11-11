# RC-505-organizer
#
# Readme here for details
# https://github.com/mjarvis1997/RC-505-organizer

import os, shutil, sys
from os.path import exists

# name of new root folder
root = "505-organized"

# if root folder already exists
if(exists(root)):
   print("ERROR: Folder named '505-organized' already exists, exiting program to avoid overwriting any existing files\nDelete or move the existing '505-organized' folder and then run again")
   sys.exit()

# create root folder
os.mkdir(root)

# function to move files from individual folders into new aggregate numbered folder
def moveSong(songNumber):

    # name of new song folder
    newFolderPath = root + "/" + str(songNumber)

    # create new folder for song
    os.mkdir(newFolderPath)

    # for each track in the current song
    for i in range(1,6):

        # construct file paths
        currFolderPath = str(songNumber).zfill(3) + "_" + str(i)
        currFilePath = currFolderPath + "/" + currFolderPath + ".WAV"

        # if folder exists for current track
        if(exists(currFolderPath)):

            # if file exists in folder
            if os.listdir(currFolderPath):

                # move file to new folder
                shutil.copy(currFilePath, newFolderPath)


def findSongs():
    # counter for number of songs
    numOfSongs = 0

    # for each song in the 505's folders
    for i in range(1,100):

        # for each track in the current song
        for ii in range(1,6):

            # construct track folder name
            folderName = str(i).zfill(3) + "_" + str(ii)

            # if folder for track exists
            if(exists(folderName)):

                # if there are files in the current folder
                if os.listdir(folderName):

                    numOfSongs += 1

                    # move WAV files for this song to new folder      
                    moveSong(i)
                    break

    print("SUCCESS: Moved files for " + str(numOfSongs) + " songs to '505-organized'")

# call main function
findSongs()