#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
input_username = input("Please enter your full name after several spaces: ") #Requests input from the user
trimmed_input = input_username.lstrip() #Removes the leading spaces
print(trimmed_input) #Prints the result