def add (a1, a2) :
    print ("The answer is " + str(a1 + a2))

def sub (a1, a2) :
    print ("The answer is " + str(a1 - a2))

def multi (a1, a2) :
    print ("The answer is " + str(a1 * a2))

def divide (a1, a2) :
    print ("The answer is " + str(a1 / a2))

def options () :
        print ("1- Add.")
        print ("2- Subtract.")
        print ("3- Multiply.")
        print ("4- Divide.")
        print ("5- Exit.")

def main () :
    run = True
    while run :
        options ()

        n1 = int(input("Choose the first number : "))
        if n1 != int :
            print ("Write a number.")
            run = False
            main ()

        n2 = int(input("Choose the second number : "))
        if n2 != int :
            print ("Write a number.")
            run = False
            main ()


        chosen = int(input("Please choose an option : "))

        if chosen == 5 :
            run = False
            exit

        if chosen == 1 :
            add (n1, n2)

        if chosen == 2 :
            sub (n1, n2)

        if chosen == 3 :
            multi (n1, n2)

        if chosen == 4 :
            divide (n1, n2)

        if chosen > 5 :
            print ("Please choose a valid option.")

main ()