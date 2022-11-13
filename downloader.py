from pytube import YouTube
from moviepy.editor import *
import datetime, os

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



def seconds_cutter(time):
    """
    returns the end_time of the track to be 
    cut from the main file in hh:mm:ss format
    """
    # convert text-based time format to seconds
    if len(time) == 2:
        time_in_sec = int(time[0]) * 60 + int(time[1])
    elif len(time) == 3:
        time_in_sec = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

    # recude seconds by 1
    time_in_sec -= 1

    # convert seconds to text-based format
    time_formatted = str(datetime.timedelta(seconds=time_in_sec))
    return time_formatted


def check_duplicate_track(name):
    if os.path.exists(name + '.mp3'):
        count = 1
        new_name = name + ' - ' + str(count) + '.mp3'
        while os.path.exists(new_name):
            count +=1
            new_name = name + ' - ' + str(count) + '.mp3' 
            new_name = new_name
        return new_name    
    else:
         return name + '.mp3'  

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

    # start time of track to save in hh:mm:ss or mm:ss format
    track_start = track_to_extract[track_to_extract.index(":")+2:]

    track_name = track_to_extract[track_to_extract.index(" ")+1:track_to_extract.index(":")-1]

    if x < len(txt_split)-1:
        # get next track details
        next_track_to_extract = txt_split[x+1]

        # start time of next track in list form
        next_track_start = next_track_to_extract[next_track_to_extract.index(":")+2:].split(":")

        track_end = seconds_cutter(next_track_start)
        
        audioclip = AudioFileClip('dummy.webm').subclip(track_start, track_end)

        name = dir_name + track_name

        name = check_duplicate_track(name)
        
        audioclip.write_audiofile(filename = name)

        audioclip.close()
        
    elif x == len(txt_split)-1:

        audioclip = AudioFileClip("dummy.webm").subclip(track_start)
        
        name = dir_name + track_name + '.mp3'

        audioclip.write_audiofile(filename = name)

        audioclip.close()
        

os.remove("dummy.webm")
# TODO 