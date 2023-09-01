# Write a python script to print the above user account object using operator 
# overloading (hint __str__method) 

class user_account:

    def __init__(self,userid,balance):
        self.userid = userid
        self.balance = balance

    def __add__(self,other):
        total_userid = self.userid + other.userid
        total_balance = self.balance + other.balance
        total = user_account(total_userid, total_balance)
        return total

    def __str__(self):
        return str(self.userid)+" : "+str(self.balance)

user1 = user_account(12,12000)
user2 = user_account(13,13000)
user3 = user_account(14,14000)

total = user1 + user2 + user3
print(total)
