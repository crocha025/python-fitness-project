def read_file():
    fp = open("user_database.txt","r")
    lines = fp.readlines()
    fp.close()
    return lines

def write_new_user(string):
    fp = open("user_database.txt","a")
    fp.write("\n")
    fp.write(string)
    fp.close()

def build_dict(lines):
    dw = dict()
    for line in lines:
        if ',' in line:
            line = line.split(',')
            line[0] = line[0].strip()
            line[1] = line[1].strip()
            k = line[0]
            v = line[1]
            dw[k] = v

    return dw

def login(dictionary):
    user_name = input("Enter the username: ")
    user_password = input("Enter the password: ")
    if user_name not in dictionary.keys():
        print("User does not exist")
        return False

    if user_password == dictionary[user_name]:
        print("Login successful")
        return True
    else:
        print("Login not successful")
        return False

def main():
    option = int(input("Choose option 1. Signup, 2. Enter your username and password to login: "))
    if option == 1:
        user_name = input("Enter the username: ")

        user_password = input("Enter the password: ")
        temp = []
        temp.append(user_name)
        temp.append(user_password)
        s = ",\t"
        temp = s.join(temp)
        write_new_user(temp)
        print("Signup successful")

    if option == 2:
        lines = read_file()
        d = build_dict(lines)
        success = login(d)

        if success:
            print("Welcome to the Fitness Program!")
        else:
            print("Please restart the program and try again.")
            exit()

def fitness_program():
    choice = input("Would you like to check the available exercises for purchase?: (Y/N)")
    if choice == "Y":
            choice = input(("The available exercises for our fitness program are endurance, strength, balance, flexibility, or 'exit' to quit. Which one would you like to proceed with? "))
            if choice == "endurance":
                print("By choosing endurance, you will obtain a collection of exercises that'll be",
                      "consisted of planks, body weight squats, walking lunges, situps, and pushups. With these exercises,",
                      "there'll be a strict schedule where you will have to keep up with the exercises. Difficulty will be increased after a few weeks",
                      "in order to challenge and test your endurance level.")
            if choice == "strength":
                print("The strength program will consist of exercises such as bent-over rows, squats, pull-ups, deaadlifts, and bridges,",
                      "in order to increase your strength ability. The difficulty will be increased about a week in.")
            if choice == "balance":
                print("The balance program will consist of exercises such as banded triplanar toe taps, single leg cross-body punches,",
                      "paloff press with rotation, and much more! Balance is an important aspect in terms of athleticism and exercise.,",
                      "The exercises will become more challenging throughout the program.")
            if choice == "flexibility":
                print("The flexibility program will consist of exercises such as standing hamstring, piriformis stretch, stretches in triceps and figure four,",
                      "side bend, and much more. The program will follow a tight schedule!")
            decision = input("Would you like to proceed to the purchase page with the current exercise category? Type 'Y' if yes. If not, you can type 'exit' to quit the program: ")
            if decision == "Y":
                trial = input("For the category exercise that you chose, this program will calculate the price based on an input of how many weeks you would like to use the program. For a small trial, it'll be 4.99/week. For a medium trial, it'll be 7.99/week and for a full trial, it'll be 10.99/week. Please type in exactly which trial you would like to purchase, eg. 'small trial', 'medium trial', 'full trial': ")
            if trial == "small trial":
                weeks = int(input("How many weeks would like to use the program for? Remember, the small trial is 4.99/week."
                                  "Please input the number of weeks you would like to use the program for: "))
                weeks = 4.99 * weeks
                print("The price for your small trial will be", weeks)
                
            if trial == "medium trial":
                weeks = int(input("How many weeks would you like to use the program for? Remember, the medium trial is 7.99/week."
                                  "Please input the number of weeks you would like to use the program for: "))
                weeks = 7.99 * weeks
                print("The price for your medium trial will be", weeks)
                
            if trial == "full trial":
                weeks = int(input("How many weeks would you like to use the program for? Remember, the full trial is 10.99/week."
                                  "Please input the number of weeks you would like to use the program for: "))
                weeks = 10.99 * weeks
                print("The price for your full trial will be", weeks)

    



    if choice == "N":
        exit()
    if decision == "N":
        exit()

main()
fitness_program()

