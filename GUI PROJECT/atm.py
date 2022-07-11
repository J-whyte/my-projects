print("Welcome\nOlumide-oke josiah")

account_balance = (1000000)

chance = 2
pin = input("Enter your pin: ")
if pin == 2019:
    print("What will you like to do ?")
while chance > -1:
    if pin != 2019:
        print(f"wrong Password try again !!!!\n{chance}Trial Remaining")
        chance = chance - 1
    print("You've Exceeded your Trial")




# while True:
#     print("press 1 for Withdrawal")
#     print("press 2 for Deposit")
#     print("press 3 for to Check Balance")
#     options = int(input("Enter selected options: "))
#     if options == 1:
#         print("You selected Withdrawal")
#         print("[$500,$1000,$10000,$15000,$20000,$40000]")
#         amount_inp = int(input("Enter amount you would like to withdraw: "))
#         withdrawal = account_balance - amount_inp
#         total = withdrawal == account_balance

#     print("Transaction Successful")
#     if options == 2:
#         print("You selected Deposit")
#         amount_dep = int(input("Enter amount you would like to Deposit: "))
#         withdrawal = account_balance + amount_dep
#         total = withdrawal == account_balance
#         print("Transaction Successful")
#
#     elif options == 3:
#          print(f"Your Available Balance is {account_balance}")
