# Write a python script to create 5 threads to fill a list with random numbers till 100.

from threading import Thread
from time import sleep
import random

l1 = []

class num20(Thread):
    global l1
    for _ in range(20):
        random_number = random.randint(1,20)
        l1.append(random_number)
        
class num40(Thread):
    global l1
    for _ in range(20):
        random_number = random.randint(21,40)
        l1.append(random_number)
        
class num60(Thread):
    global l1
    for _ in range(20):
        random_number = random.randint(41,60)
        l1.append(random_number)
        
class num80(Thread):
    global l1
    for _ in range(20):
        random_number = random.randint(61,100)
        l1.append(random_number)

class num100(Thread):
    global l1
    for _ in range(20):
        random_number = random.randint(81,100)
        l1.append(random_number)

num1 = num20()
num2 = num40()
num3 = num60()
num4 = num80()
num5 = num100()

num1.start()
num2.start()
num3.start()
num4.start()
num5.start()

print("List:",l1)