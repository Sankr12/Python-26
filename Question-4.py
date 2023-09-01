# Write a python script to create two threads. first thread will print all
# Even numbers and second thread will print all odd numbers till 100

from threading import Thread
from time import sleep

class Even_numbers(Thread):
    def run(self):
        total = 0
        for i in range(1,51):
            total+=i
            sleep(2)

class Odd_numbers(Thread):
    def run(self):
        total=0
        for i in range(51,101):
            total+=i
            sleep(2)

num1 = Odd_numbers()
num2 = Even_numbers()

num1.start()
sleep(1)
num2.start()

num1.join()
num2.join()