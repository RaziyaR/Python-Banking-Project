class Bank:
    def __init__(self,accno,accname,username,password,balance=0):
        self.accNo=accno
        self.accholder=accname
        self.uname=username
        self.pwd=password
        self.balance=balance

    def Login(self,un,pw):
        if((self.uname==un)and(self.pwd==pw)):
            return True
        else:
            print("Login unsuccessfull")
    def deposit(self,depAmount):
        if(depAmount<0):
            print("Invalid amount")
        else:
            self.balance=self.balance+depAmount
            print(depAmount,"successfully deposited")

    def withdraw(self,withamount):
        if(withamount>self.balance):
            print("Insufficient balance")
        else:
            self.balance=self.balance-withamount
            print(withamount,"Successfull withdrawn")

    def Accountdetails(self):
        print("Account Number:",self.accNo)
        print("Account Holder:",self.accholder)
        print("Account Balance:",self.balance)
        return


print("Welcome\n##########")
username=input("Enter the username:")
password=input("Enter the password:")
b1=Bank('123456',  'razi123', 'razi123', 'password')
if(b1.Login(username,password)):
    print("Login successfull")
    while (True):
        option=int(input("############\n1.Deposit\n2.Withdraw\n3.Account Details\n4.Exit\nEnter an option:"))
        if option==1:
            depositAmt=int(input("Enter the amount to deposit:"))
            b1.deposit(depositAmt)
        elif option==2:
            withdrawAmt=int(input("Enter the amount to withdraw:"))
            b1.withdraw(withdrawAmt)
        elif option==3:
            b1.Accountdetails()
        elif option==4:
            print("Thank you for banking")
            exit()
        else:
            print("Invalid option")