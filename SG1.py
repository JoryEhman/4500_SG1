# noinspection SpellCheckingInspection
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
        This was helpful in the design structure of the validateInt method. The rubric demands that different
        cases should be handled if the user input for N and/or R are incorrect. The while loop needs to find and
        check for cases such as A)is the value entered a number? if not, then we need to call it out B)If it is a number
        then we need to check that it is an integer. C) Lastly, we need to check that the value is within the intended range
    - https://www.geeksforgeeks.org/python/python-string-isnumeric-method/
        This link was also used for the above reasons. It was helpful in understanding how to check for if the value was "valid"
"""

import random

# print_program() prints out the introduction message to users, explaining what will be asked of them, and what
# they should expect to see as a result.
def print_program() -> None:
    program_explanation = (
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

    print(program_explanation)

#validateInt is the function that validates user input at the start of the program. It takes in 2 arguments: min_value
#and max_value. These values correspond to the range (inclusive) that the user's input should allow. The parameters
#passed will be hardcoded in main, to correspond with the valid input values for N and R.
def validate_int(min_value: int, max_value: int) -> int | None:
    while True:
        user_input = input() #Reads in user input (is a string)

        try:
            number = float(user_input) #attempts to convert to a float
        except ValueError: #If a value that cannot be converted to a float is found, error printed
            print("Error: Your input must be a number")
            print("Please enter a valid number:")
            continue

        if not number.is_integer(): #Checks that the value number is actually an integer, negative or not
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

def run_all_simulations(N: int, R: int) -> None:

    #final_whole_pill_tracker keeps a list of each day the final whole pill was removed from the bottle
    final_whole_pill_tracker = []

    #loops once for every simulation based on R simulations
    for simulation in range(R):

        #the number of whole pills left in the bottle
        whole_pills = N

        #the number of half pills left in the bottle
        half_pills = 0

        #how many days it took to empty the bottle of every whole_pill and half_pill
        days_to_empty = 0

        #flag for determining if the final whole pill was removed
        final_whole_pill_taken = False

        #loops until both half pills and whole pills are both fully removed
        while whole_pills > 0 or half_pills > 0:

            #this conditional checks for the existence of half pills and whole
            #pills in the bottle to determine what choice of pill is available to remove
            if whole_pills > 0 and half_pills > 0:
                #makes use of the random.choices() function to weight whole pill or half pill heavier
                #based on how many are left in the bottle
                choice = random.choices(['whole', 'half'], [whole_pills, half_pills])[0]
            elif whole_pills > 0:
                choice = 'whole'
            else:
                choice = 'half'

            #conditional to calculate what to do when either whole or half pill is chosen
            if choice == 'whole':
                whole_pills -= 1
                half_pills += 1

                # checks for the first time whole pills is 0 after taking a whole pill
                #and tracks the day with the final_whole_pill_tracker
                if whole_pills == 0 and final_whole_pill_taken == False:
                    final_whole_pill_tracker.append(days_to_empty)
                    final_whole_pill_taken = True

            else:
                half_pills -= 1

            #increases by one each day until loop ends to track how many days
            #each simulation takes to empty the entire bottle
            days_to_empty += 1

    create_histogram(final_whole_pill_tracker)

#uses text based histogram to display some interesting analysis of what day the final pill
#was removed from the bottle and how frequently it occurred across all the simulations
def create_histogram(data):
    occurrences = {}

    #add one to the "value" for each final_day "key" occurrence
    for final_day in data:
        occurrences[final_day] = occurrences.get(final_day, 0) + 1

    #sort the values in the occurrences dictionary before printing them out
    sorted_days = sorted(occurrences)

    #this section adds some limits to what can be displayed so the histogram
    #does not extend too far outside the limits of the console
    max_days = max(occurrences.values())
    max_line_width = 50
    scale = max(1, max_days // max_line_width)

    print("\nHistogram: Day Last Whole Pill Removed")
    print("Day | Frequency")
    print("--------------------------------------------------")

    #loops for each "key" in the sorted_days and prints a meaningful line to the console
    #indicating how frequent the day the final pill was removed over all the simulations
    for final_day in sorted_days:
        print(f"{final_day} | {'#' * (occurrences[final_day] // scale)} ({occurrences[final_day]})")

if __name__ == "__main__":
    print_program()
    print("Enter an integer N (1-1000):")
    N = validate_int(1, 1000)
    print("Enter an integer R (1-10000):")
    R = validate_int(1, 10000)
    print("You have selected for " + str(N) + " pills and " + str(R) + " simulations to be ran")
    run_all_simulations(N, R)