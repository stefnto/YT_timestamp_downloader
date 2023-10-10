from pytube import YouTube
from moviepy.editor import *
from func import *
import re

# get Youtube video
youtube_link = input("Enter youtube link: ")

yt = YouTube(youtube_link)

vid_title = yt.title + '.webm'

# download highest quality 'webm' stream of video
yt.streams.get_audio_only('webm').download(filename="dummy.webm")

if os.path.exists(str("dummy.webm")):
    print("File exists!")
else:
    print("File does not exist")    

f_path = input("Enter timestamps .txt file path: ")
f = open(f_path, "r")
txt = f.read()

# regex patterns
time_pattern = r'(\d{2}:\d{2}:\d{2})|(\d{2}:\d{2})|(\d:\d{2})'
special_char_pattern = r'[\/:?"<>|-]|\s*[\\/:?"<>|-]\s*'

# get each line as a list item
txt_split = txt.split("\n")

# make new directory for the audio files
dir_name = input("Enter the path to the folder to save the audio files: ")

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print("Made new directory!")
else:
    print("Directory already exists")    

for x in range(len(txt_split)):
    
    # select track
    track_to_extract = txt_split[x]
    
    # get track timestamp info in tuple
    track_info = re.search(time_pattern, track_to_extract)
    if track_info is None:
        exit("ERROR: String \'" + track_to_extract + "\' resulted into None object.\nExiting...")
    
    # start time of track to save in hh:mm:ss or mm:ss format
    track_start = track_info.group()
    
    if track_info.span()[0] == 0: # time at start of string
        track_name = track_to_extract[track_info.span()[1]:]
    else:
        track_name = track_to_extract[:track_info.span()[0]]
        
    track_name = re.sub(special_char_pattern, "", track_name)
      
    if x < len(txt_split)-1:
        # get next track details
        next_track_to_extract = txt_split[x+1]

        next_track_info = re.search(time_pattern, next_track_to_extract)
        if next_track_info is None:
            exit("ERROR: String \'" + next_track_to_extract + "\' resulted into None object.\nExiting...")
            
        # start time of next track in list form
        next_track_start = next_track_info.group().split(":")
        track_end = seconds_cutter(next_track_start)
        
        audioclip = AudioFileClip('dummy.webm').subclip(track_start, track_end)
        
        name = dir_name + "\\" +  track_name
        name = check_duplicate_track(name)
        
        audioclip.write_audiofile(filename = name)
        audioclip.close()
    
    # last clip
    elif x == len(txt_split)-1: 

        audioclip = AudioFileClip("dummy.webm").subclip(track_start)
        
        name = dir_name + "\\" +  track_name
        name = check_duplicate_track(name)
        
        audioclip.write_audiofile(filename = name)
        audioclip.close()
        
os.remove("dummy.webm")