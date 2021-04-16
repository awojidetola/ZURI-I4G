class Budget:
    def __init__(self, category=['Food','Clothing','Entertainment'], balance=[0,0,0]):
        self.category=category
        self.balance=balance
        print ("Please take note of the categories:")
        print ("0: Food")
        print ("1: Clothing")
        print ("2: Entertainment")
    
    def Deposit(self):
        try:
            Category=int(input("Enter a category from the list above: \n"))
            while Category not in [0,1,2]:
                print ("Please enter 0,1 or 2 to continue")
                Category=int(input("Enter a category from the list above: \n"))
            userAmount=int(input("Enter the amount you would like to Deposit \n"))
            self.balance[Category]=self.balance[Category]+userAmount
        except ValueError:
            print ("Invalid")
        else:
            print ("Thank you for depositing {}, your current balance for {} is N {}".format(name,self.category[Category],self.balance[Category]))
            
    def Withdrawl(self):
        try:
            Category=int(input("Enter a category from the list above: \n"))
            while Category not in [0,1,2]:
                print ("Please enter 0,1 or 2 to continue")
                Category=int(input("Enter a category from the list above: \n"))
            userAmount=int(input("How much would you like to Withdrawl? \n"))
            while userAmount>self.balance[Category]:
                print ('Insufficient Funds')
                userAmount=int(input("How much would you like to withdrawl? \n"))
            self.balance[Category]=self.balance[Category]-userAmount
        except ValueError:
            print ("Invalid!")
        else:
            print ("Thank you for Banking with us {}, your current balance for {} is N {}".format(name,self.category[Category],self.balance[Category]))
            
    def Balance(self):
        try:
            Category=int(input("Enter a category from the list above: \n"))
            while Category not in [0,1,2]:
                print ("Please enter 0,1 or 2 to continue")
                Category=int(input("Enter a category from the list above: \n"))
        except ValueError:
            print ("Invalid!")
        else:
            print ("Your Balance for {} is currently N {}".format(self.category[Category],self.balance[Category]))
 
    def Transfer(self):
        try:
            Category=int(input("Enter a category from the list above: \n"))
            while Category not in [0,1,2]:
                print ("Please enter 0,1 or 2 to continue")
                Category=int(input("Enter a category from the list above: \n"))
            CategoryA=int(input("Select the category you want to transfer from: "))
            CategoryB=int(input("select the Category you wnat to transfer to: "))
            while CategoryA==CategoryB:
                print ("Please try again, you cannot transfer to the same category")
                CategoryA=int(input("Select the category you want to transfer from: "))
                CategoryB=int(input("select the Category you wnat to transfer to: "))
            userAmount=int(input('Enter the amount you would like to transfer: '))                    
            self.balance[CategoryA]=self.balance[CategoryA]-userAmount
            self.balance[CategoryB]=self.balance[CategoryB]+userAmount
        except ValueError:
            print ("Invalid!")
        else:
            print ("N {} has been transferred from {} to {}".format(userAmount,self.category[CategoryA],self.category[CategoryB]))

print ("The Buget App")
name=input("Hello there!, What is your name?\n")
print ("Welcome ",name)
myBudget = Budget()
print ("What do you want to do")
print ("1. Deposit")
print ("2. Withdrawl")
print ("3. Check your balance")
print ("4. Transfer")
print ()
try:
    Input = int(input("Please, enter an option to continue: "))
    while Input not in [1,2,3,4]:
        Input=int(input("Please enter an option from 1 to 4 to continue: "))
    else: 
        if Input== 1:
            myBudget.Deposit()
        elif Input==2:
            myBudget.Withdrawl()
        elif Input==3:
            myBudget.Balance()
        elif Input==4:
            myBudget.Transfer()
    
    while Input not in [1,2,3,4]:
        Input=int(input("Please enter an option to continue: "))
        
except ValueError:
    print ("Invalid!")

