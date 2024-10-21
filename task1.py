print("welcome to atm".center(50,'*'))
accounts={}
current_user=""
def checknum(s):
    c=0
    for i in s:
        if i>='0' and i<='9':
            c+=1
    return c
def create():
    s=input("enter card number:")
    if len(s)!=16 or checknum(s)!=16:
        print("Invalid card number")
        while True:
            s=input("enter card number:")
            if len(s)!=16 or checknum(s)!=16:
                print("Invalid card number")
                continue
            break
    if s in accounts:
        print("Account already exists...")
        return
    while True:
        pin=input("set 4 digit pin:")
        if checknum(pin)!=4:
            print("enter valid pin!!")
            continue
        pindup=input("re-enter your pin:")
        if pin==pindup:
            break
        print("pin mismatch!!!")
        continue
    accounts[s]=[pin,0]
    print("(:ACCOUNT CREATED SUCCESSFULLY:)".center(50,'*'))
def login():
    s=input("enter card number:")
    if len(s)!=16 or checknum(s)!=16:
        print("Enter valid card number")
        while True:
            s=input("enter card number:")
            if len(s)!=16 or checknum(s)!=16:
                print("Enter valid card number")
                continue
            break
    if s not in accounts:
        print("Account doesnot exist...")
        return
    while True:
        pin=input("enter 4 digit pin:")
        if checknum(pin)!=4:
            print("enter valid pin!!")
            continue
        checkpin=accounts[s][0]
        if checkpin==pin:
            print("Login SUCCESSFULLY".center(50,'*'))
            return s
        else:
            print("enter correct pin!!")
            continue
def check(s):
    if s=="":
        print("Login to check balance!".center(50,'*'))
        return
    print("Available balance:",accounts[s][1])
def credit(s):
    if s=="":
        print("Login to credit!".center(50,'*'))
        return
    while True:
        mny=input("enter amount:")
        if checknum(mny)!=len(mny):
            print("enter valid amount")
            continue
        mny=int(mny)
        accounts[s][1]=accounts[s][1]+mny
        print("SUCCESFULLY COMPLETED".center(50,'*'))
        break
    return
def withdraw(s):
    if s=="":
        print("Login to withdraw amount!".center(50,'*'))
        return
    while True:
        mny=input("enter amount:")
        if checknum(mny)!=len(mny):
            print("enter valid amount")
            continue
        mny=int(mny)
        if mny>accounts[s][1]:
            print("Insufficient Balance!!!")
            return
        accounts[s][1]=accounts[s][1]-mny
        print("SUCCESFULLY COMPLETED".center(50,'*'))
        break
while True:
    print("click \n1 to create account\n2 to login\n3 to check balance\n4 to credit amount\n5 to withdraw\n6 to exit\n7 to terminate program")
    n=int(input("enter your choice:"))
    if n==1:
        create()
    elif n==2:
        current_user=login()
    elif n==3:
        check(current_user)
    elif n==4:
        credit(current_user)
    elif n==5:
        withdraw(current_user)
    elif n==6:
        if current_user=="":
            print("NO ACCOUNT EXIST".center(50,'*'))
        else:
            print("LOGGED OUT...THANKYOU".center(50,'*'))
        current_user=""
    elif n==7:
        print("program terminated!!!")
        break
    else:
        print("):sorry!! enter valid choice:(")
    continue
