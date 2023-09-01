# Write a python script to join 2 threads after printing completing the first Question.

from threading import Thread
from time import sleep

class Even_numbers(Thread):
    def run(self):
        total = 0
        for i in range(1, 51):
            total += i
            sleep(2)
        print("Even_numbers thread completed.")

class Odd_numbers(Thread):
    def run(self):
        total = 0
        for i in range(51, 101):
            total += i
            sleep(2)
        print("Odd_numbers thread completed.")

num1 = Odd_numbers()
num2 = Even_numbers()

num1.start()
sleep(1)
num2.start()

# Join both threads after they complete their tasks
num1.join()
num2.join()

print("Main thread exiting.")
