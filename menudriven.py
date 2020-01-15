

def print_menu():
	
	print("\nMenus\n\
		* Enter 1 to add\n\
		* Enter 2 to print names\n\
		* Enter 3 to exit")

def get_user_input_and_do_function():
	
	user_choice = int(input("\nPlease see the above menus options and tell me what i have to do now :"))
	
	if user_choice == 1:
		names.append(input("\nOk I will add your name.. Please enter the name to add : "))
		print("\nEntered name added ..")

	elif user_choice == 2:
		print("\nOkie I will display the names you are added")
		for x in names:
			print(x)

	elif user_choice == 3:
		print("\nThank you for using me!! Byee ...")
		
	else:
		print("\nSorry I'm not getting please enter it again..")
	
	return user_choice	

names = []
loop = True
print("Hi User I'm a simple python program to add your names i will save it and view those names if you wish\n\n")

while loop:
	print_menu()
	user_choice = get_user_input_and_do_function()
	if  user_choice == 3:
		break
	input()
