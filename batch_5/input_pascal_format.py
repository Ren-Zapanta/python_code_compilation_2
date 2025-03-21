#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
user_input = input("Please enter your full name: ") #Requests the user for their name
pascal_reformat = user_input.title().replace(" ", '') #Converts input to pascal casing by using title and replace method
print(pascal_reformat) #Prints reformatted input
