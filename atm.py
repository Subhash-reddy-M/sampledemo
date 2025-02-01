user_name="subhash reddy"
pass_word="python12"

user_name=input("enter your name: ")
pass_word = str(input("enter your password:"))

user_name==user_name
pass_word==pass_word
print('''
1.Deposite
2.withdraw
3.Ministatement
4.Exit
''')
amount=100000
choice=int(input("slect your opition: "))
if choice==1:
    deposite=int(input("Enter the amount: "))
    amount+=deposite
    print("Total amount:",amount)
elif choice==2:
     withdraw=int(input("enter your amount: "))
     amount-=withdraw
     print("Total amount:",amount)
elif choice==3:
    print("-------ATM----------")
    print("user_name: ",user_name)
    print("Total amount: ",amount)
    print("thank you for visitiing")
    print("--------------------")
elif choice==4:
    exit()

else:
    print("please enter correct logins")