The provided CLI downloader trims the downloaded youtube audio into .mp3 files according to the timestamps provided.

Provide a .txt with the timestamps. For now "XX. {name} : {timestamp} " format is supported, where XX is the possible track name which is not saved, name the name of the sub-track and timestamp a "hh:mm:ss" or "mm:ss" time format

The script uses the libraries pytube and moviepy which need to be pip installed


TODO

Support video file trimming,
Flexible timestamp formats,
Provide executable ?