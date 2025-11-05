# Nested conditions = A conditional statement has other conditional
# statements within it. conditions inside 




def sandwichstore():

    print("welcome to ian foods. what would you like?")
    print("1. meatball snawich")
    print("2. turkey sandwich")
    print("3. honey turkey sandwich")
    print("4. buffallo chicken")
    print("5. surprise me (mystery sandwich)")
    selection = int(input("please select your main food item?"))
    if selection == 1:
        print(" youve selected the meatball snawich.")
        print("what sides do u want?")
        print("1. fries")
        print("2. salad")
        print("3. chips")
        side = int(input())
        if side ==1:
            print("great meatball and fries")
        elif side == 2:
            print("healthy meatball and chips")
        elif side == 3:
            print("nice, meatball and chips")


sandwichstore()
def atm():
    balance = 2000
    pin = 1234

    userpin = input("please type in yout bank pin number:")
    if userpin == pin:
        print("welcome. what would you like to do?")
        print('1. withdraw money')
        print("2. deposit money")
        print("3. check your balance")
        selection = int(input())
        if selection == 1:
            amount = int(input("how much do you want to take out?"))
            if amount > balance:
                print("sorry, you dont have that much in your account")
            else:
                newbalance = balance- amount
                print('your new balance is :' + str(newbalance))
        else:
            print("sorry incorrect.")
            atm()

        atm()

