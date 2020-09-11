import random
import time
import sys

print('Welcome To fastrack USSD Banking Project...')
time.sleep(8)

def sub_airtime_others( ):
    print("###################################################")
    amt=input("Please enter destination phone line or last four digits if the number :")
    print(" ")
    print("00. Back\n0. Main")  
    if amt.isdigit( ) and amt == 11 or amt == 4:
        time.sleep(5)
        print("Transaction is been processed")
    elif amt== "00":
        airtime_self( )
    elif amt == "0":
        main( )	
    
def  airtime_others( ) :
	print("###################################################")
	prompt = input("Please enter your PIN:")
	
	print("0. Main")
	if prompt.isdigit( ) and len(prompt)==4:
	    sub_airtime_others( )
	elif prompt == "0":
	    main( )    
	    
def sub_airtime_self( ):
    print("###################################################")
    amt=input("Please enter amount (50 - 10000):")  
    print("00. Back\n0. Main")  
    if amt.isdigit( ) and amt == 50 or amt <= 10000:
        time.sleep(5)
        print("USSD loading...")
        time.sleep(5)
        print("Transaction is been processed")
    elif amt== "00":
        airtime_self( )
    elif amt == "0":
        main( )	
        			
def  airtime_self( ):
	print("###################################################")
	prompt = input("Please enter your PIN:")
	
	print("0. Main")
	if prompt.isdigit( ) and len(prompt)==4:
	    sub_airtime_self( )
	elif prompt == "0":
	    main( )										
																#--------------------------------------------------												
###i'm yet to catch an error for non -digit and more than one digit###REMINDER!!!						#-#------------------------------------------------------								
# This is the function for options.
def main( ) :
	print("1. Airtime-Self\n2. Airtime-Others\n3. Transfer-UBA\n4. Transfer-Other Banks\n5. Transfer-UBA Prepaid\n6. Check Bakance\n7. Pay Bills\n8. Next")
	choice=input("\n ")
	print("__________________________")
	print("###################################################")
	if choice == "1":
		time.sleep(10)
		airtime_self( )
	elif choice == "2":
		time.sleep(10)
		airtime_others( )
	elif choice =="3":
		time.sleep(10)
		balance( )
	elif choice =="4":
		time.sleep(10)
		transf( )
	elif choice =="5":
		time.sleep(10)
		funds( )
	else:
		time.sleep(5)
		print("Not an option.")
		sys.exit( )
		
# This is the function which prompts the user as to whether the user wishes to continue or stop transaction.
def exit( ):
	exit= input("Do you wish to make another transaction [Y/N] :")
	if exit== "N":
		sys.exit( )
	elif exit == "#":
	    main( )
	else:
		log_in( )
		
# This is the function for logging using the fast code *919#			
def log_in( ):
    try:
        a=0
        while a<3:
            a+=1
            print("###################################################")
            USSD=input("ENTER USSD:")
            if(USSD !="*919#"):
            	 print("please re-enter USSD ...")
            else:
            	print("###################################################")
            	print("Welcome to our online services how may we help you")
            	main( ) 
            	exit( )
        else:
        	time.sleep(10)
        	print("checking discrepancies...")
        	time.sleep(5)
        	print("An error has occured.")
    
    except:
    		sys.exit( )
    		
log_in( )