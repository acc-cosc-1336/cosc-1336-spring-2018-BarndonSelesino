from src.assignment.assignment4 import factorial
def main():#void function
    '''
    Create a loop that'll run until the user doesn't type the letter 'y'
    In the loop,
    Capture one number from the keyboard and validate for a range between 1 and 10.
    Call the factorial function.
    Save the result to a variable.
    Print the variable value.

    Ask the user if they want to continue.

    TO RUN YOUR PROGRAM GO TO IN PYTHON IDLE RUN->RUN MODULE.
    IN THE PYTHON SHELL TYPE main()

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    dont_stop = 'y'
    while dont_stop == 'y':
        num = int(input("Please enter a letter that isn't y:     "))
        while num < 0 or num > 10:
            print('Invalid')
            num = int(input('Please enter number:     '))
        answer = factorial(num)
        print(answer)

        dont_stop = input("would you like to continue")  

                  
                    
                  




#another option to run the program is to call the main() function below and Run->Run Module
main()
