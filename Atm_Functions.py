import random

database={2949768861:'Password',1234567891:'Olori'}

def bankOperations():
    print ("Please select an Option:")
    print ("1: Withdraw")
    print ("2: Deposit")
    print ("3: Complaint")
    
    userOption = int(input('Please select an option:\n'))
    
    if userOption==1:
        def Withdrawl():
            try:
                userAmount=int(input ('How much would you like to withdraw?\n'))
                account_balance=accountBalance()
                if userAmount>account_balance:
                    print ("Insufficient Funds")
                    TryAgain=str(input ("Would you like to try again or log out? Press 1 to Try Again, Another Key to Log Out \n"))
                    if TryAgain=='1':
                        Withdrawl()
                    else:
                        logout()
            
                    
                else:
                    account_balance=account_balance-userAmount
                    print ("Your Balance is: {}".format(account_balance))
                    print ("Take out Your Cash!")
            except ValueError:
                print('Invalid Entry')
                TryAgain=str(input ("Would you like to try again or log out? Press 1 to Try Again, Another Key to Log Out \n"))
                if TryAgain=='1':
                    Withdrawl()
                else:
                    logout()  
                         
        Withdrawl()
            
    elif userOption==2:
        def Deposit():
            try:
                userDeposit=int(input("How much would you like to deposit?\n"))
                account_balance=accountBalance()
                account_balance=account_balance+userDeposit
                print ("Your Balance is: {}".format(account_balance))

            except ValueError:
                print("Invalid Entry!")
                TryAgain=str(input ("Would you like to try again or log out? Press 1 to Try Again, Another Key to Log Out \n"))
                if TryAgain=='1':
                    Withdrawl()
                else:
                    logout()                         
        Deposit()
                    
    elif userOption==3:
        def Complaint():
             userReport=input ('What is the issue you would like to report?\n')
             print ('Thank you for contacting us')
        Complaint()
                    
    else:
        print ("Invalid Entry, please try again!")
        TryAgain=str(input ("Would you like to try again or log out? Press 1 to Try Again, Another Key to Log Out \n"))
        if TryAgain=='1':
            bankOperations()
        else:
            logout()
            
    anotherOperation=str(input("Would you like to perform another Operation? Press 1 for Another Operation, Any other key to Log Out\n"))
    if anotherOperation == '1':
        bankOperations()
    else:
        logout()
        
def accountBalance():
    return 1000

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    print ("Thank you for Banking with us!")

def TryAgain():
    TryAgain=str(input("Would you like to try again or log out? Press 1 to Try Again,  Another Key to Log Out \n"))
    if TryAgain == '1':
        login()
    else:
        logout()

def login():
    print ("********** LOGIN IN HERE! **********")
    try:
        AccountNumber=int(input("Please enter your account number here!\n"))
        if AccountNumber in database.keys():
            passcode=input("Enter your password here:\n")
            if passcode==database[AccountNumber]:
                print ("Successful Login!")
                bankOperations()
            else:
                print ("Incorrect Password!")
                TryAgain()
        else:
            print ("Account Number not found!")
            TryAgain()
            
    except ValueError:
        print ("Error in Connection!")
        TryAgain()
        
def register():
    print ("********** REGISTER HERE! **********")
    first_name=input("Enter your first name here!\n")
    last_name=input("Enter your last name here!\n")
    email=input("Enter your email here!\n")
    password=input("Enter your password here!\n")
    print ("Welcome!", first_name + " " + last_name)
    accountNumber=generateAccountNumber()
    print ("Your account number is: "+str(accountNumber))
    print ("Make sure you remember your password!\n")
    print ("You have received N1000 as New Customer incentive!")
    database[accountNumber]=password
    login()
    
def init():
    print ("********** WELCOME TO BANK ZURI **********")
    haveAccount=str(input("Please do you have an account with us? 1. Yes 2. No \n"))
    if haveAccount=='1':
        login()
    elif haveAccount=='2':
        register()
    else:
        print ("You have selected a Wrong Option!")
        TryAgain=str(input ("Would you like to try again or log out? Press 1 to Try Again, Another Key to Log Out \n"))
        if TryAgain=='1':
            init()
        else:
            logout()

init()     