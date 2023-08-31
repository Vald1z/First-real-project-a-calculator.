import random

def main() :
    while True :
        if True :
            try :
                numbers = int(input("Choose a positive number : "))
                mine = random.randint(0, numbers)
            except ValueError :
                print ("Write correctly please.")
                continue

        print ("I've chosen a number between 0 and " + str(numbers) + ".")
        guess = int(input("Take a guess : "))

        if guess == mine :
            print ("Nice guess !")
            choice = input ("Play agian (y/n) ? ")

            if choice == "y" :
                main()

            if choice == "n" :
                break
        else :
            print ("Sorry, wrong guess.")
            print ("I choose " + str(mine) + ".")
            choice2 = input ("Try agian (y/n) ? ")
            
            if choice2 == "y" :
                main()

            if choice2 == "n" :
                break

main ()