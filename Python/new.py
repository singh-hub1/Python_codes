initial_balance=5000;
withdraw_ammount = int(input("Enter your withdraw amount?"))
if ((withdraw_ammount % 5 == 0) and (initial_balance > withdraw_ammount )):
    print('YOUR BALENCE IS:', (initial_balance - (withdraw_ammount + 0.50)))

else:
    print('YOUR BALENCE IS:', (initial_balance))