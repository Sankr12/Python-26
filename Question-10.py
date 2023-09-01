import threading

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    temp = num
    sum_of_cubes = 0
    num_digits = len(str(num))
    
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** num_digits
        temp //= 10
    
    return num == sum_of_cubes

class PrimeChecker(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        if is_prime(self.num):
            print(f"{self.num} is a prime number.")
        else:
            print(f"{self.num} is not a prime number.")

class ArmstrongChecker(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        if is_armstrong(self.num):
            print(f"{self.num} is an Armstrong number.")
        else:
            print(f"{self.num} is not an Armstrong number.")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    prime_checker = PrimeChecker(num)
    armstrong_checker = ArmstrongChecker(num)

    prime_checker.start()
    armstrong_checker.start()

    prime_checker.join()
    armstrong_checker.join()

    print("Main thread exiting.")
