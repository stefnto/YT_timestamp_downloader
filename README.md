The provided CLI downloader trims the downloaded youtube audio into .mp3 files according to the timestamps provided.

Provide the youtube video link, a .txt with the timestamps and names of each track (usually provided in the youtube description or the comments) and the path to the folder to save (folder will be made if doesn't exist)
The name of track will not include any special characters \/:?"<>| or '-' that might connect the timestamp with the name.
For example the timestamp '10:53 - Name123?' will result in a track with the name 'Name123' that starts from the minute 10:53.

The script uses the libraries pytube and moviepy which need to be pip installed

TODO

Support video file trimming,
Provide executable ?