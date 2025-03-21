#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
user_input = input("Please input a statement: ") #Requests a statement from the user as the input.
word_count = len(user_input.split()) #Splits the statement using spaces to determine word count.
print(f"There are {word_count} words in your statement.") #Prints the number of words present in the input