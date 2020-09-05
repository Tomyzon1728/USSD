#from random import randint
import time
import sys

print('Welcome To fastrack USSD Banking Project...')
time.sleep(8)

bank_list="""
1. Access Bank
2. Fidelity Bank
3. Guarantee Trust Bank
4. Heritage Bank
5. Polaris Bank
6. Stanbic IBTC
7. Unity Bank
8. Wema Bank
"""

gen_bvn = " "

def BVN_checker( ):
    global gen_bvn
    bvn = [str(i) for i in range (5)]
    gen_bvn= "".join(bvn)
    print (gen_bvn)
       				
def open_acct( ):
	global gen_bvn
	print("Welcome to our online Account opening services.")
	print("loading...")
# creating an empty list to serve as a temporary place holder.
	temp_storage= [ ]
	f_name= input("Enter your first name:")
	s_name= input ("Enter your second name:")
	sex = input("Enter sex [M/F]:")
	BVN_checker( )
	temp_storage.append(f_name)
	temp_storage.append(s_name)
	temp_storage.append(sex)
	temp_storage.append(gen_bvn)
	details= " ".join(temp_storage)
	print(details)
	exit( )
	
def upgrade_migrate( ):
		print("Welcome to our online Upgrade/Migration services.\n 1. Ugrade\n 2. Migrate")
		prompt = int(input("Enter preferred Choice:"))
		if prompt==1:
			time.sleep(5)
			print("Upgrading...")
			exit( )
		elif prompt == 2:
			time.sleep(5)
			print("Migrating...")
			exit( )
		elif prompt == "#":
			options_menu( )
		else:
			sys.exit( )

def balance ( ):
	print("ACCOUNT\tBALANCE\n CHECKER")
	print("press 0 is go back to the Main Menu.")
	pin=input("Enter your 4 digit pin:")
# isdigit( ) is used to  check for digits within a str while the nested if is used to make sure the user inputs 4 digits.

###```i am to put the pin trial in a while loop```###REMINDER!!!

	if len(pin)!=4:
	   	print("Make sure its a 4digit pin.")
	   	time.sleep(5)
	   	balance( )
	else:
	   		    if pin.isdigit( )==True:
	   		        time.sleep(5)
	   		        print("Loading...")
	   		        exit( )
	   		    elif pin== "#":
	   		        options_menu( )
	   		    else:
	   		        time.sleep(15)
	   		        print("wrong pin")
	   		        sys.exit( )
		
def transf( ):
	print("1. Transfer self\n2. Transfer others")
	trnsf=input(":")
	if trnsf == "1":
	    time.sleep(5)
	    print("Sending...")
	    exit( )
	elif trnsf=="2":
	    time.sleep(5)
	    num=int(input("Enter receivers mobile number:"))
	    print("Transferring to",num)
	    exit( )
	else:
	    if trnsf.isdigit( )!= True:
	        time.sleep(5)
	        print("Not an option")
	        sys.exit( )
	    elif trnsf.isdigit( )==True and len(trnsf)>2:
	        time.sleep( 5)
	        print("wrong password.")
	        sys.exit( )
	    else:
	        time.sleep(10)
	        print("An error has occurred")
	        sys.exit( )
	        	
def funds( ):
	time.sleep(3)
	print(bank_list)
	bnk = input("Select receipients Bank:")
	acc_num= input("Entet account number:")
	print("Sending to",acc_num)
	exit( )													

def options_menu( ) :
	print("1. Open Account\n2. Upgrade/Migrate\n3. Balance\n4. Transfer\n5. Funds")
	choice=int(input("Enter an option:"))
	if choice == 1:
		time.sleep(10)
		open_acct( )
	if choice == 2:
		time.sleep(10)
		upgrade_migrate( )
	elif choice ==3:
		time.sleep(10)
		balance( )
	elif choice ==4:
		time.sleep(10)
		transf( )
	elif choice ==5:
		time.sleep(10)
		funds( )
	else:
		time.sleep(5)
		print("Not an option.")
		sys.exit( )

def exit( ):
	exit= input("Do you wish to make another transaction [Y/N] :")
	if exit== "N":
		sys.exit( )
	else:
		log_in( )
				
def log_in( ):
    try:
        a=0
        while a<3:
            a+=1
            USSD=input("ENTER USSD:")
            if(USSD !="*919#"):
            	 print("please re-enter USSD ...")
            else:
            	print("Welcome to our online services how may we help you")
            	options_menu( ) 
            	exit( )
        else:
        	time.sleep(10)
        	print("checking discrepancies...")
        	time.sleep(5)
        	print("An error has occured.")
    
    except:
    		sys.exit( )
    		
log_in( )