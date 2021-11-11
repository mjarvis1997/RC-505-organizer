# RC-505-organizer
Organizes audio files for songs created on the RC-505

## Context
The Boss RC-505 is a looper station - it stores up to 99 songs which each have 5 individual tracks.

You can connect a computer to the RC-505 and retrieve the WAV files for each song, but the file structure is not ideal
### RC-505 File Structure
```
.
├── 001_1                    # songNumber_trackNumber
│   └── 001_1.WAV            # songNumber_trackNumber.WAV
├── 001_2
│   └── 001_2.WAV
├── 001_3
│   └── 001_3.WAV
└── ...
```

Because the 505 stores tracks in separate folders, aggregating them can be a pain. We would prefer that the tracks for a given song all be in the same folder.

### Output structure:
```
.
├── 001                      # songNumber
|   ├── 001_1.WAV            # songNumber_trackNumber.WAV
|   ├── 001_2.WAV
|   ├── 001_3.WAV
|   ├── 001_4.WAV
│   └── 001_5.WAV
├── 001_2
|   ├── 002_1.WAV            # songNumber_trackNumber.WAV
|   ├── 002_2.WAV
|   ├── 002_3.WAV
|   ├── 002_4.WAV
│   └── 002_5.WAV
└── ...
```

## Usage
1. Move RC-505 folders into a new folder on your device using USB cable
2. Move 505-organize.py into the folder containing the RC-505 folders
3. Call the python script
```
python3 505-organize.py
```
4. Folders will now be sorted per-song inside '505-organized' folder
