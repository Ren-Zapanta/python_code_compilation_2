#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
user_input = input("Please enter your name in incorrect casing: ") #Requests input from the user
format_input = user_input.title() #Reformats the user input to title format
print(format_input) #Prints the result