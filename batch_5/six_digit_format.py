#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
user_input = int(input("Please input a number (0-1000): ")) #Asks the user for input
formatted_number = f'{user_input:06d}' #Formats input to 6 digits
print(formatted_number) #Prints result
