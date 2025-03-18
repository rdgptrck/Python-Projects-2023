name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go either left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to the river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam accross and got eaten by an alligator.")
    elif answer == "walk":
        print("You walked for hours, ran out of water and found a haunted looking house. Type enter to enter the house or walk to walk away and continue your journey.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back to the main road and got run over by a car.")
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you want to talk to them (yes/no)? ")

        if answer: == "yes"
            print("You talked to the stranger and gave you gold. You win!")
    elif answer == "no"
            print("You ignored the stranger and they were offended and suddenly stabbed you at the heart.You lose!")
    else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for playing", name)