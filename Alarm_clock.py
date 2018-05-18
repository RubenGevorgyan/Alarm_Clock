import datetime
import os
import time
import random
import webbrowser



def check_alarm_input(alarm_time):
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and alarm_time[1] < 60 and alarm_time[1] >= 0 and alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False

def input_time():
    print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
    while True:
        alarm_input = input(">> ")
        try:
            alarm_time = [int(n) for n in alarm_input.split(":")]
            if check_alarm_input(alarm_time):
                break
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Enter time in HH:MM or HH:MM:SS format")
    return  alarm_time
def time_claculator(seconds_hms,alarm_time):
    alarm_seconds = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
    return alarm_seconds
def current_time(seconds_hms):
    now = datetime.datetime.now()
    current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])
    return current_time_seconds
def alarm_on(time_diff_seconds):
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
    link = input("Please put the Youtube link of the song you want to wake up")
    time.sleep(time_diff_seconds)
    print("Wake Up!")
    webbrowser.open_new(link)
def main():
    alarm_time=input_time()
    seconds_hms = [3600, 60, 1]
    remaining_time=time_claculator(seconds_hms,alarm_time)-current_time(seconds_hms)
    if remaining_time < 0:
        remaining_time += 86400
    alarm_on(remaining_time)
main()
