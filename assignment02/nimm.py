"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    stones = 20
    num_player = 1

    while (stones > 0):
        print(f"There are {stones} stones left")
        take = int(input(f"Player {num_player} would you like to remove 1 or 2 stones? "))

        # check user usage
        while take != 1 and take != 2:
            take = int(input("Please enter 1 or 2: "))
        stones -= take

        # change player
        if (num_player == 1):
            num_player += 1
        else:
            num_player -= 1
        print("")

    print(f"Player {num_player} wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
