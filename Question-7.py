'''Write a python script to create a clock where 1st thread will print the current time
every second and 2nd will print “1 Minute Completed” after every 1 minute.'''

from threading import Thread
from time import sleep, strftime

class CurrentTime(Thread):
    def run(self):
        while True:
            current_time = strftime("%H:%M:%S")
            print(f"Current Time: {current_time}")
            sleep(1)

class MinuteNotifier(Thread):
    def run(self):
        while True:
            sleep(60)
            print("1 Minute Completed")

time_thread = CurrentTime()
minute_notifier_thread = MinuteNotifier()

time_thread.start()
minute_notifier_thread.start()

time_thread.join()
minute_notifier_thread.join()
