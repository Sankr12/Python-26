# Write a python script to change the name of the thread

from threading import Thread, current_thread
from time import sleep

class RenameThread(Thread):
    def run(self):
        old_name = current_thread().name
        print(f"Thread name before renaming: {old_name}")

        # Change the name of the thread
        current_thread().name = "NewThreadName"
        new_name = current_thread().name
        print(f"Thread name after renaming: {new_name}")

        # Simulate some work
        total = 0
        for i in range(1, 51):
            total += i
            sleep(2)

if __name__ == "__main__":
    # Create a thread with an initial name
    my_thread = RenameThread(name="OriginalThreadName")

    # Start the thread
    my_thread.start()

    # Wait for the thread to finish
    my_thread.join()

    print("Main thread exiting.")
