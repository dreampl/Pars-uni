import time
import winsound

def convert_to_seconds(time_input):
    time_parts = time_input.split(":")
    if len(time_parts) == 1:  # ورودی ثانیه
        return int(time_parts[0])
    elif len(time_parts) == 2:  # ورودی دقیقه:ثانیه
        minutes = int(time_parts[0])
        seconds = int(time_parts[1])
        return minutes * 60 + seconds
    elif len(time_parts) == 3:  # ورودی ساعت:دقیقه:ثانیه
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])
        hours = int(time_parts[0])
        
        return hours * 3600 + minutes * 60 + seconds
    else:
        return 0