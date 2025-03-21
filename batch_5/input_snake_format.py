#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
user_input = input("Please input your full name in incorrect casing: ") #Requests user for their name
snake_reformat = user_input.lower().replace(" ", "_") #Uses .lower() and .replace() methods to convert input to snake case
print(snake_reformat) #Prints result