import time
import itertools #This lets us create all possible combinations of numbers to guess the password.
import string #This gives us access to pre-built groups of characters, like digits (0123456789)

def digitBruteForce(password, length): #creates function that take in two inputs
    # Character pool (adjust for only digits)
    characters = string.digits  # Only digits for simplicity
     
    print("\nStarting brute force attack... This may take some time for complex passwords.\n") #\n = new line
    time.sleep(3) #program stops running for the amount of seconds u choose inside the (), so the user gave time to read the text
    start_time = time.time() #start timing #use time.perf_counter() when you need more precision like microseconds or millisecond-level accuracy.
    attempts = 0 #set number os attemps to 0
    # Try combinations of the specified length
    for attempt in itertools.product(characters, repeat=length): # ".product" creates every possible combination of numbers (0-9) with the given length (4 or 6).
        attempts += 1 #counts the number of attempts the program took until got it right
        attempt = ''.join(attempt) # Converts the combination of numbers into a single string, makes a list of strings into a single one and '' means its a blank string
        print(f"Trying: {attempt}")  # Show every attempt being made  # f-Strings let us put variables inside a text
        if attempt == password: 
            end_time = time.time() #saves the time when the password was found
            print(f"\nPassword cracked! It was: {attempt}")
            print(f"Time taken: {end_time - start_time:.2f} seconds with {attempts} attempts") # ".2f" indicates a number must be printed with 2 decimals
            print("This is intended to demonstrate how adding complexity makes cracking harder.")
            return #stops the function 

    print("\nPassword not found. Increase character pool or ensure the password matches the length.") #just in case the password is not found

def pswCracker(): 
    while True: #starts a loop until user wants to exit 
        # Ask the user for the password length
        while True:
            try:
                length_choice = int(input("Choose the password length (4 or 6 numbers only): "))
                if length_choice in [4, 6]: #if this is true it runs line 40
                    break #stops the while loop (line 29)
                else:
                    print("Please choose either 4 or 6.")
            except ValueError: # "execpt" lets us decide how to react to an error, in this case "ValueError", which is when the user input a string instead of an int
                print("Invalid input. Please enter 4 or 6.")

        # Get the password from the user
        password = input(f"Enter the password to test brute force cracking ({length_choice} NUMBERS): ") #gets the value that was input in line 31

        # Check if the password matches the chosen length
        if len(password) != length_choice or not password.isdigit(): #check if the length of the password is the same as the length choosen, "or not" makes sure that even if the password length matches the length choosen it will still run anothe rcondition which in this case is to check if the password is all int (se a senha nao tem o mesmo tamanho OU a senha nao e tudo em digito) #cant be "and" because if it doesnt match the first condition (meaning it has the proper length) it wont check the second condition leading the program to not work properly
            print(f"Error: The password must be exactly {length_choice} numbers long and must have no characters.")
        else:
            digitBruteForce(password, length_choice)

        # Ask if the user wants to try another password or exit
        while True:
            try_again = input("\nDo you want to try another password? (yes/no): ").strip().lower() #".strip" by itself removes whitespacing (characters with empty value like tabs or spaces) and ".lower()" converts the string into lower cases (to prevent the user from writing in caps and the code causing an error)
            if try_again in ["yes", "y"]: #if true runs the first while true again (line 27)
                break 
            elif try_again in ["no", "n"]:
                print("Goodbye!")
                return #ends the first while loop (line 27), meaning the program ended
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

# Run the program
if __name__ == "__main__": #if someone imports my program (and if my code didnt have "if __name__ == "__main__":") everything inside it would run automatically on import, but now for using "if __name__ == "__main__":" they need to specifally call each function they want to use "brute force attack" or "pswCracker", but in this program specifically, the pswCracker function is calling the brutw force attack function, so all the functions would work even if u call only pswCracker. # this is how it should look like when calling this program from another file "from digitsPasswordCracker import pswCracker" (next line) pswCracker()
    pswCracker()