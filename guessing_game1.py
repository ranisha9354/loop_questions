i=1
while i<=5:
    user=int(input("Enter your number between 1 to 10:"))
    my_number=6
    if user<my_number:
        print("Your number is lessthen my number:")
    elif user>my_number:
        print("Your number is greater then my number:")
    elif user==my_number:
        print("Congralations! your guess is correct:")
        break
    print("yr... your guess is incorrect")
    i=i+1



    