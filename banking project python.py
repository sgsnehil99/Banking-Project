import pandas as pd 
fn=[]
ln=[]
un=[]
pwd=[]
bal=[]
cre=[]
deb=[]
em=[]
print ('already a user : log in')
print ('new user :sign up')
choice =input('enter you choice')
if((choice=='signup') or (choice=='sign up') or (choice=='SIGNUP') or (choice=='SIGN UP')):
    firstname=input('enter first name')
    lastname=  input('enter last name')
    username=input('enter the username')
    if(un.count(username)==1):
        username=input('username already exist therefore enter other username')
    password=input('enter the password with 1 capital,1 no,1 symbol & 8 characters')
    email=input('enter a valid email id')
    fn.append(firstname)
    ln.append(lastname)
    un.append(username)
    pwd.append(password)
    cre.append(10000)
    deb.append(0)
    bal.append(10000)
    data={'firstname':fn,
          'lastname':ln,
          'username':un,
          'password':pwd,
          'credit':cre,
          'debit':deb,
          'balance':bal
          }
    df=pd.Dataframes(data)
    df.to_csv('BANK DETAILS.csv')
elif((choice=='login')or(choice=='LOGIN')or(choice=='log in')or(choice=='LOG IN')):
    username=input('enter your username')
    if(un.count(username)==1):
        p=un.index(username)
        pd=input("enter your password")
    else:
        print('username incorrect')
    if(pwd[p]==pd):
        print("you are logged in")
        print("1:debit \n 2:credit \n 3:change password \n 4:transfer \n 5:logout")
        n=int(input("enter the no which list your choice"))
        if (n==1):
            print("enter the ammout of withdrawn")
            debit=int(input("amount:"))
            deb[p]=deb[p]+debit
            bal[p]=bal[p]-debit
        elif(n==2):
            print("enter the amount deposited")
            credit=int(input("amount:"))
            cre[p]=cre[p]+credit
            bal[p]=bal[p]+credit
        elif(n==3):
            print("are you sure you want to change password code 1 for yes 0 for no")
            i=int(input("enter the code"))
            if(i==1):
                new_pd=input('enter new password')
                n_p=input('enter the new password again')
                if(new_pd==n_p):
                    pwd[p]=new_pd
                    print("your new password is updated")
        elif(n==4):
            print("enter the username to which the amount has to be transfered")
            una=input("the amount reciever username is:")
            if(un.conunt(una)==1):
                pos=un.index(una)
                am=int(input("enter the amount to be  tarnsfered:"))
                cre[pos]=cre[pos]+am
                deb[p]=deb[p]+am
                bal[pos]=bal[pos]+am
                bal[p]=bal[p]-am
            else:
                print("the username to which the amount is to be transfered is invalid")
            
##        else:
            #break
elif((choice!='login')or(choice!='LOGIN')or(choice!='log in')or(choice!='LOG IN')and (choice!='signup') or (choice!='sign up') or (choice!='SIGNUP') or (choice!='SIGN UP')):
    print("invalid choice")
##    break