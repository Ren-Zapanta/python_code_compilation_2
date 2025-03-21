#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
user_input = input("Please enter your name in incorrect casing: ") #Requests input from the user
format_input = user_input.swapcase() #Reformats the user input by swapping the input casing
print(format_input) #Prints the result