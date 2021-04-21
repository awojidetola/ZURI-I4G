import datetime

Time=datetime.datetime.now()

print ("The current time and date is: ",Time.strftime("%Y-%m-%d %H:%M:%S") )
print ("--------------------------------------------------------------------")
usersList=['Seyi','Bamidele','Ojo','Matthew']
usersPasscode=['Seyi123','Bamidele123','Ojo123','Matthew123']
userName=input("Welcome! What is your name?\n")

if userName not in usersList:
    print ('Hello, you are not permitted to use this service')
    
else:
    print ("Hello "+userName)
    
    userCode=input("Enter your passcode: \n")
    userId=usersList.index(userName)
    
    
    if (userCode!=usersPasscode[userId]):
        print ('Wrong Password!')
    else:
        def bankOperations():
            print('Please select an Option')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')

        selectedOption = int(input('Please select an option:'))
        
        if selectedOption==1:
            print ('You selected Withdrawl')
        elif selectedOption==2:
            print ("You selected Cash Deposit")
        elif selectedOption==3:
            print ("You selected Complaint")
        else:
            print ("Check you selection again")
            
        if selectedOption==1:
            
            def Withdrawl():
                userAmount=input("How much would you like to withdraw?\n")
                print ("Dear " +userName+' take out your cash')
     
        elif selectedOption==2:
            def Deposit():
                previousBalance=0
            try:
                userDeposit=int(input("How much would you like to deposit?\n"))
                previousBalance+userDeposit
            except ValueError:
                print("Invalid Entry!")
            else:
                print ('Dear '+userName+' your current balance is: #',userDeposit+previousBalance)
                
        elif selectedOption==3:
            def Complaint():
                userReport=input ('Dear '+userName+' What is the issue you would like to report?\n')
                print ('Dear '+userName+' Thank you for contacting us')
            
        else:
            print ("Invalid Entry, please try again!")
            
        print ("Thank you for banking with us")
        print ("--------------------------------------------------------------------")
        print ("The current time and date is: ",Time.strftime("%Y-%m-%d %H:%M:%S") )
