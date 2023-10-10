import datetime, os

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
    """
    if name exists return name with counter incremented
    """
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