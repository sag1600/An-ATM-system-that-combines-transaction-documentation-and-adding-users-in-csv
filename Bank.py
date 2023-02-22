import csv
from datetime import datetime
import time

def ReadAccounts():
   red_a_lis= []
   red_a='accounts.csv'
   with open(red_a) as accounts:
    num_data = csv.reader(accounts,delimiter=',')
    for i in num_data:
       red_a_lis.append(i)
       continue
   return red_a_lis
       
def ReadTransactions():
   red_t2 = []
   red_t= 'transaction.csv'
   with open(red_t) as transaction:
     red_data = csv.reader(transaction,delimiter=',')
     for  j in red_data:
      red_t2.append(j)
   return red_t2
 
def Init():
    global red_a_lis ,red_t2
    red_a_lis=ReadAccounts()
    red_t2=ReadTransactions()
    return red_a_lis,red_t2
   
def SaveAccounts(red_a_lis): 
    file = open('accounts.csv','w',newline='')
    writer =csv.writer(file,dialect='excel',)
    r_file =csv.reader('accounts.csv')
    file = ['accounts.csv']
    file.clear()
    for file in red_a_lis:
     if r_file != red_a_lis:
         writer.writerow(file)
   
def SaveTransaction(red_t2):
   o_fill = open('transaction.csv','w',newline='') 
   o_fill_w=csv.writer(o_fill,dialect='excel')
   t_file =csv.reader('transaction.csv')
   o_fill= ['transaction.csv']
   o_fill.clear()
   for o_fill in red_t2:
     if t_file != red_t2:
         o_fill_w.writerow(o_fill)
   
def Save():
    SaveAccounts(red_a_lis)
    SaveTransaction(red_t2)
     
def Menu():
   print("\nGood Morning\n")
   print(f"""1)Creating a new account """)
   print(f"""2)Account deposit""")
   print(f"""3)Withdrawal from the bank account""")
   print(f"""4)Check cash balance""")
   print(f"""5)Bank account transaction report""")
   print(f"""6)Exit\n""")
   Main()

def Add_account():
    global red_a_lis
    for j in range(1):
        try:
          new_add_1 = input(f"""Please enter the "Name" of the account holder: """)
          x= new_add_1.isnumeric()
          if  x == True :
             print("The value you entered is incorrect")
             time.sleep(2)
             Menu()
          new_add_2= int (input("Please enter the account number: "))
        except:
            print("The value you entered is incorrect")
            Menu()

    new_add_2=str(new_add_2)
    Bal = 0 
    new_add=[new_add_2,str(Bal),new_add_1]
    for i in red_a_lis:
            if i[0]  == new_add[0]:
             print(f"""\nThe account exists, try again\n""")
             time.sleep(3)
             Menu()

    red_a_lis.append(new_add)
    SaveAccounts(red_a_lis)
    print()
    print(new_add)
    time.sleep(4)
    Menu()
    
def Deposit():
   print()
   global red_a_lis ,red_t2
   for j in range(1):
     try:
       dep = input((f"Please enter a bank account number: "))
       x =dep.isalpha()
       if  x==True:
          print("You entered an invalid value. Please try again")
          time.sleep(2)
          Menu()

       dep_2= (int(input("Please enter an amount to deposit:  ")))
     except:
         print("You entered an invalid value. Please try again")
         time.sleep(2)
         Menu()
   for i in red_a_lis:
        if i[0]== [dep][0]:
            print()
            print(f"""The previous amount of money in the bank:         {i}""")
            new_num = i[1]
            num = float(new_num)
            num_1 = int(num)
            i.remove(i[1])
            sum = dep_2 + num_1
            sum1 = str(sum) 
            break
            
   else:
     print("The number is in the system")
     time.sleep(2)
     Menu()

   new_lis_move_1=[i[0],sum1,i[1]]
   red_a_lis.remove(i)
   red_a_lis.append(new_lis_move_1)
   date_1= datetime.now()
   date_2 =date_1.strftime("%d/%m/%Y %H:%M ")
   new_lis_2 = [i[0],date_2,sum1]
   red_t2.append(new_lis_2)
   SaveTransaction(red_t2)
   SaveAccounts(red_a_lis)
   print(f"""The amount of money in the bank after the update: {new_lis_move_1}""")
   print(f"Updating the new deposit movement in the bank:    {new_lis_2}")
   print()
   time.sleep(5)
   Menu()
      
def Withdraw():
    print()
    global red_a_lis ,red_t2
    number_acc = input("Pleas Enter Account Number: ")
    x =number_acc.isalpha()
    if  x==True:
          print("You entered an invalid value. Please try again")
          time.sleep(2)
          Menu()

    for i in range(1):
        try:
          number_wit = int(input("Please enter an amount to withdraw: "))
          if number_wit <0:
               print("\nמYou cannot enter a negative value")
               time.sleep(2)
               Menu()
        except:
         print("\nThe value you entered is incorrect, please enter a number only")
         time.sleep(2)
         Menu()

    for i in red_a_lis:
            if i[0] == [number_acc][0]:
                print()
                print(f"""The previous amount of money in the bank:         {i}""")
                new_money = i[1]
                new_money_1 = float(new_money)
                new_money_2 = int(new_money_1)
                sum = new_money_2-number_wit
                if sum <0:
                    print("\nNot enough money balance")
                    time.sleep(2)
                    Menu()
                else:
                    sum1 = str(sum)
                    break 
            continue  
    else:
     print("\nThe bank account does not exist in the system")
     exit()
    new_acc =[i[0],str(sum1),i[2]]
    red_a_lis.remove(i)
    date_1= datetime.now()
    date_2 =date_1.strftime("%d/%m/%Y %H:%M ")
    sum_2 = -number_wit-new_money_2%number_wit
    sum_3 = str(sum_2)
    new_move = [number_acc, date_2 ,sum_3]
    red_t2.append(new_move)
    red_a_lis.append(new_acc)
    SaveAccounts(red_a_lis)
    SaveTransaction(red_t2)
    print()
    print(f"""The amount of money in the bank after the update: {new_move}""")
    print(f"Updating the new deposit movement in the bank:    {new_acc}")
    time.sleep(3)
    Menu()

def Balance():
    print()
    num_acc = input("Pleas Enter Account Number: ")
    x = num_acc.isalpha()
    if x == True:
        print("\nThe value you entered is incorrect, please enter a number only")
        time.sleep(2)
        Menu()
    global red_a_lis 
    Init()
    for i in red_a_lis:
        if i[0]==[num_acc][0]:
            print(i)
            Menu()
    else:
            print("\nBank account number not found")
            time.sleep(2)
            Menu()

def Report():
    print()
    global red_t2
    num_acc_r = (input("Enter your number account: "))
    x = num_acc_r.isalpha()
    if x == True:
        print("\nThe value you entered is incorrect, please enter a number only")
        time.sleep(2)
        Menu()

    for i in red_a_lis:
        if i[0]==[num_acc_r][0]:
            print("Number   Current balance  withdrawal/deposit ")
            for j in red_t2:
                if j[0]==[num_acc_r][0]:
                    print(j)
            print(end="") 
            Menu()
    else:
         print("\nBank account number not found")
         time.sleep(2)
         Menu()

def Main():
    global red_a_lis,red_t2
    red_a_lis,red_t2 = Init()
    for i in range(1):
     try:
      choice = int( input("\nPlease enter your choice from the menu: ") )
     except:
         print("\nYour selection is incorrect. Please choose between the numbers 1-6\n")
         time.sleep(2)
         Menu()
     if choice == 1:
        Add_account() 
     if choice ==2:
         Deposit()
     if choice == 3:
         Withdraw()
     if choice == 4:
         Balance()
     if choice == 5:
            Report()
     if choice == 6:
            print("\nThank you very much, hello and goodbye")
            Save()
            exit()
     if choice >6 or <=0:
            print("\nYour selection is incorrect. Please choose between the numbers 1-6\n")
            time.sleep(2)
            Menu()
Menu()
