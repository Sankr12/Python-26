# Write a python script to create 2 threads to add all the 
# values from 1 to 100

from threading import Thread
from time import sleep

total_sum = 0

class add_odd(Thread):
    global total_sum
    for i in range(1,101,2):
        total_sum+=i

class add_even(Thread):
    global total_sum
    for i in range(2,101,2):
        total_sum+=i

num1 = add_odd()
num2 = add_even()

num1.start()
num2.start()

num1.join()
num2.join()

print(total_sum)