import re

DIFFICULTIES = {
    "easy": {
        "rounds": 5,
        "min": 0,
        "max": 10
    },
    "medium": {
        "rounds": 10,
        "min": 0,
        "max": 10
    },
    "hard": {
        "rounds": 5,
        "min": 0,
        "max": 10
    },
    "extreme": {
        "rounds": 5,
        "min": 0,
        "max": 10
    }
}

regex = "^[1-5]{1}$"

def main_menu():

    print("Welcome to NumberGuessing\n")
    print("Select one option:")
    print("1. Help")
    print("2. Rules")
    print("3. Settings")
    print("4. Start game")
    print("5. Exit")
    while True:
        option = input("Select: ")
        if re.search(regex, option):
            break
        else:
            print("Please select the correct option")

def main():
    main_menu()

if __name__ == "__main__":
    main()
