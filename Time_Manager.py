import time
import winsound

def pomodoro_timer(duration, break_duration, num_pomodoros):
    for i in range(num_pomodoros):
        print("System  Running...")
        countdown(convert_to_seconds(duration))
        print("\n" + (" " * 20))  # اضافه کردن فضای خالی
        play_sound()
        print("Break Time:")
        countdown(convert_to_seconds(break_duration))
        play_sound()
    print("All Done")

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print()  # اضافه کردن فاصله بعد از چاپ زمان

def play_sound():
    # پخش صدا
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)

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

# تست با 2 دوره کاری به مدت 3 ثانیه و 1 ثانیه استراحت
a=int(input('tedad dore kar:'))
c=input('modat zamane kar:')
b=input('modat zamane esterahat:')
pomodoro_timer(c, b, a)
