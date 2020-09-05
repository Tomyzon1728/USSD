import time
import sys

print('Welcome To fastrack USSD Banking Project...')
time.sleep(8)

BankList="""
Select the Bank you wish to Transfer to:
1. Access Bank
2. Fidelity Bank
3. Guarantee Trust Bank
4. Heritage Bank
5. Polaris Bank
6. Stanbic IBTC
7. Unity Bank
8. Wema Bank"""

	
def open_acct( ):
	temp_storage= [ ]
	f_name= input("Enter your first name:")
	s_name= input ("Enter your second name:")
	sex = input("Enter sex [M/F]:")
	temp_storage.append(f_name)
	temp_storage.append(s_name)
	temp_storage.append(sex)
	print(temp_storage)
	
def upgrade_migrate( ):
		print("Welcome to our online Upgrade/Migration services.\n 1. Ugrade\n 2. Migrate")
		prompt = input("Enter preferred Choice:")
		if prompt==1:
			time.sleep(5)
			print("Choose Upgrade choice.")
		else:
			time.sleep(5)
			print("Choose Migration Choice:")

def balance ( ):
	pass				

def options ( ) :
	print(" 1. Open Account\n2. Upgrade/Migrate\n3. Balance\n4. Transfer\n5. Recharge")
	choice=int(input("Enter an option:"))
	if choice == 1:
		print("Welcome to our online Account opening services.")
		print("loading...")
		time.sleep(10)
		open_acct( )
	if choice == 2:
		time.sleep(10)
		upgrade_migrate( )
	if choice ==3:
		time.sleep(10)
		balance( )
		
		
		
	

def main( ):
    try:
        a=0
        while a<3:
            a+=1
            USSD=input("ENTER USSD:")
            if(USSD !="*919#"):
            	 print("please re-enter USSD ...")
            else:
            	print("Welcome to our online services how may we help you")
            	options( )
            	sys.exit( )
        else:
        	sys.exit( )
    
    except:
    	time.sleep(10)
    	print("checking discrepancies...")
    	time.sleep( 5)
    	print("An error has occured.")	

main( )

	

	
		
			
					
"""
choice=input('Choose your preferred option:')
if(choice=="1"):
    print('Welcome to Open Account option')
    print("Press 0 if you don't have a BVN")
    returncode=input("Please Enter Your BVN:")
    if(returncode=="0"):
        print("Kindly visit our nearest branch to register for your BVN")
        print("For more info call: +2348132558019. Thank you.")
    else:
        print("The BVN you entered is incorrect, kindly visit the nearest branch to resolve this issue. Thank you.")
elif(choice=="2"):
    print("This feature will soon be available. Thank you.")
elif(choice=="3"):
    print("Your Balance is: N000,000.00")
    #print('Go to our nearest Bank to deposite a preferred amount')
    print("Thank you.")
elif(choice=="4"):
    print('Welcome to Transfer option')
    print("Enter 's' for Self and 'o' for Others")
    returncode=input()
    if (returncode=="o"):
        print(BankList)
        returncode=input()
        if (returncode=="1"):
            print("Enter Third Party Account Number:")
            print("Reply 0 to Start-Over")
            returncode=input()
            if (returncode=="0"):
                print(options)
            else:
                print("Enter Amount to Transfer")
                print("Reply 0 to Start-Over")
                returncode=input()
                if (returncode=="0"):
                    print(options)
                else:
                    print("Transfer to Third-Party was Successful")

        else:
            print("Enter Third Party Account Number:")
            print("Reply 0 to Start-Over")
            returncode=input()
            if (returncode=="0"):
                print(options)
            else:
                print("Enter Amount to Transfer:")
                print("Reply 0 to Start-Over")
                returncode=input()
                if (returncode=="0"):
                    print(options)
                else:
                    print("Transfer to Third-Party was Successful")
    else:
        print("Enter your Account Number:")
        print("Reply 0 to Start-Over")
        returncode=input()
        if (returncode=="0"):
            print("select an option")
            print(options)

        else:
            print("Enter Amount to Transfer:")
            print("Reply 0 to Start-Over")
            returncode=input()
            if (returncode=="0"):
                print("select an option")
                print(options)

            else:
                print("Transfer Done Successfully. Thank you.")
elif(choice=="5"):
        print("Enter 1 for SELF and 2 for THIRD-PARTY")
        returncode=input()
        if (returncode=="1"):
            print("Enter Preferred Amount")
            print("Reply 0 to Start Over")
            returncode=input()
            if (returncode=="0"):
                print(options)
            else:
                print("Your SELF Recharge was done Successfully. Thank You.")
        else:
            print("Enter THIRD-PARTY mobile number")
            print("Reply 0 to Start Over")
            returncode=input()
            if (returncode=="0"):
                print(options)
            else:
                print("Enter Preffered Amount")
                print("Reply 0 to Start Over")
                returncode=input()
                if (returncode=="0"):
                    print(options)
                else:
                    print("Rechard for THIRD-PARTY was successful. Thank You.")

else:
    print("Unrecognised USSD; Kindly input a correct one. Thank you.")
"""