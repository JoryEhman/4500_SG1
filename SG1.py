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

if __name__ == "__main__":
    print_program()