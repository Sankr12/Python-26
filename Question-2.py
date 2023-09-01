# Write a python script to create a user account class with 2 instance variables (userid and balance).
# Create 3 user objects and add all the user using method overloading. 

class user_account:

    def __init__(self,userid,balance):
        self.userid = userid
        self.balance = balance

    def __add__(self,other):
        total_userid = self.userid + other.userid
        total_balance = self.balance + other.balance
        total = user_account(total_userid + total)
        return total

user1 = user_account(12,12000)
user2 = user_account(13,13000)
user3 = user_account(14,14000)

total = user1 + user2 + user3
