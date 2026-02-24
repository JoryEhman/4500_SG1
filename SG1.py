"""
Programming Language: Python 3.8.3
Development Environment: PyCharm Community Edition (will test in Thonny)

CMP_SCI-4500-001
Group Members:
- Jory Ehman
- Mira Ysabela Ifurung
- Jacob Schaefer
- Ray Rulifson
- Shounak Banerjee

External Resources used:
    - https://www.geeksforgeeks.org/python/python-try-except/
        This was helpful in the design structure of the validateInt method. The rubric indicates the necessary
    - https://www.geeksforgeeks.org/python/python-string-isnumeric-method/
"""


# print_program() prints out the introduction message to users, explaining what will be asked of them, and what
# they should expect to see as a result.
def print_program() -> None:
    programExplanation = (
        "This program simulates the class Pill Puzzle.\n"
        "\nYou start with N whole pills in a bottle. Each day, either a (W)hole or (H)alf pill\n"
        "will be chosen from the assortment of pills being stored in the \"magical pill bottle.\""
        "\n\t-If you pick a whole pill (W), it must be broken in half, one half\n"
        "\t is consumed, and the other half is returned to the pill bottle.\n"
        "\t-If you pick a half pill (H), then you must consume it\n"
        "\nYou will be prompted to enter:\n"
        "\tN (1 - 1000): the starting number of whole pills in the bottle\n"
        "\tR (1 - 10000): the number of simulations that the program will run\n"
        "\nThis program illustrates interesting statistical phenomenon, by simulating many trials.\n"
        "")

    print(programExplanation)

#validateInt is the function that validates user input at the start of the program. It takes in 2 arguments: min_value
#and max_value. These values correspond to the range (inclusive) that the user's input should allow. The parameters
#passed will be hardcoded in main, to correspond with the valid input values for N and R.
def validateInt(min_value: int, max_value: int) -> int:
    while True:
        user_input = input() #Reads in user input (is a string)

        try:
            number = float(user_input) #attempts to convert to a float
        except ValueError: #If a value that cannot be converted to a float is found, error out
            print("Error: Your input must be a number")
            print("Please enter a valid number:")
            continue

        if not number.is_integer(): #Checks that the value number is actually a number, negative or not
            print("Error: Your input must be an integer")
            print("Please enter a valid number:")
            continue

        #Converts the float to an integer if it passes the non-numeric check
        number = int(number)

        #If the value falls outside the valid range, tell the user
        if number < min_value or number > max_value:
            print("The number you have entered: " + str(user_input) + " falls outside the valid range.")
            print("Please enter a valid number:")
            continue

        return number #returns the now validated answer

if __name__ == "__main__":
    print_program()
    print("Enter an integer N (1-1000):")
    N = validateInt(1, 1000)
    print("Enter an integer R (1-10000):")
    R = validateInt(1, 10000)
    print("You have selected for " + str(N) + " pills and " + str(R) + " simulations to be ran")