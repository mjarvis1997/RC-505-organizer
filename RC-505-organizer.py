# RC-505-organizer
#
# Readme here for details
# https://github.com/mjarvis1997/RC-505-organizer
#

import os, shutil, sys
from os.path import exists
from pydub import AudioSegment

# name of new root folders
d_root = "505-organized"
d_stems = d_root + "/stems"
d_masters = d_root + "/masters"

# global vars
mode = "0"
stemsFolderPath = ""
numOfTimesToRepeat = 1

# if root folder already exists
if(exists(d_root)):
   print("ERROR: Folder named '505-organized' already exists, exiting program to avoid overwriting any existing files\nDelete or move the existing '505-organized' folder and then run again")
   sys.exit()

def createFolderForSongStems(songNumber):

    # set path of curr stems folder
    global stemsFolderPath
    stemsFolderPath = d_stems + "/" + str(songNumber)

    # create the folders
    os.mkdir(stemsFolderPath)

def exportMaster(songNumber, tracks, numOfTracks):
    
    if numOfTracks == 1:
        tracks[0].export(d_masters + "/" + str(songNumber) + ".mp3", format="mp3")

    if numOfTracks > 1:

        # figure out the longest loop
        longestTrackLength = 0.0
        for track in tracks:
            if track.duration_seconds > longestTrackLength:
                longestTrackLength = track.duration_seconds

        # scale tracks to make them equally long
        scaledTracks = []
        for track in tracks:
            currTrackLength = track.duration_seconds

            # what factor to multiply this track by
            currTrackRatio = int(round(longestTrackLength / currTrackLength))
            scaledTracks.append(track * currTrackRatio)
        
        # store first scaled track in master
        master = scaledTracks[0]

        # overlay rest of scaled tracks to master
        for i in range(1, numOfTracks):
            master = master.overlay(scaledTracks[i], position = 0)

        # loop the track based on user selection
        global numOfTimesToRepeat        
        master = master * numOfTimesToRepeat

        # export master
        master.export(d_masters + "/" + str(songNumber) + ".mp3", format="mp3")

# function to move files from individual folders into new aggregate numbered folder
def findTracksForSong(songNumber):

    # create folder for song stems
    createFolderForSongStems(songNumber) 

    # array to store audio tracks as we find them
    tracks = []

    # for each track in the current song
    for i in range(1,6):

        # construct file paths
        currFolderPath = str(songNumber).zfill(3) + "_" + str(i)

        # if folder exists for current track
        if exists(currFolderPath):

            # determine if the folder is empty
            currFolderContents = os.listdir(currFolderPath)
            folderIsntEmpty = len(currFolderContents)
            
            if(folderIsntEmpty):

                # mode 0 - only moves files that have default names
                if mode == '0':

                    # determine if the folder contains a file with the expected name
                    expectedFilePath = currFolderPath + "/" + currFolderPath + ".WAV"
                    fileHasExpectedName = exists(expectedFilePath)

                    if fileHasExpectedName:
                    
                        # copy file to new folder
                        shutil.copy(expectedFilePath, stemsFolderPath)

                        # add track to our list
                        tracks.append(AudioSegment.from_wav(expectedFilePath))
                        
                # mode 1 - moves files with custom names as well
                elif mode == '1':

                    actualFilePath = currFolderPath + "/" + currFolderContents[0]
                    
                    # copy file to new folder
                    shutil.copy(actualFilePath, stemsFolderPath)
                    
                    # add track to our list
                    tracks.append(AudioSegment.from_wav(actualFilePath))

    numOfTracks = len(tracks)

    print("song #: " + str(songNumber) + " | found " + str(numOfTracks) + " tracks")

    # if we found tracks for this song
    if numOfTracks:

        # export mp3 master that combines the tracks
        exportMaster(songNumber, tracks, numOfTracks)
        return 1
    else:
        return 0

def findSongs():

    # let user choose config
    global mode 
    mode = input("Please choose desired mode:\n0: Only move file names that match the default RC-505 naming style\n1: Move all files no matter what their name is\n")
    global numOfTimesToRepeat
    numOfTimesToRepeat = int(input("Would you like to extend the length of the masters? \nEnter the number of times the loop should repeat\n(1 is default)\n"))

    # create root folders
    os.mkdir(d_root)
    os.mkdir(d_masters)
    os.mkdir(d_stems)
    
    # count number of songs added
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

                    # attempt to move WAV files for this song to new folder      
                    if(findTracksForSong(i)):
                        numOfSongs += 1

                    # move on to next song
                    break

    if numOfSongs > 0:
        print("SUCCESS: Moved files for " + str(numOfSongs) + " songs to '505-organized'")
    else:
        print("FAILURE: No valid files found" )

# call main function
findSongs()