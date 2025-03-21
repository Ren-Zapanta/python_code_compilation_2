#Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.
user_input = input("Please input a statement: ") #Requests a statement from the user as the input.
char_count = len(user_input) #Determines character count within the input.
print(f"There are {char_count} words in your statement.") #Prints the number of characters