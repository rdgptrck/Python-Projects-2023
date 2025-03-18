print("Welcome to The Ultimate Itsfunneh Quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's start :)")
score = 0

answer = input("What game does Funneh play the most? ").lower()
if answer == "roblox":
    print('Correct!')
    score += 1
else: 
        print("Incorrect!")

answer = input("What's Funneh's fam called? ").lower()
if answer == "krew":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many siblings does Funneh have? ").lower()
if answer == "4":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Where are Funneh and the Krew from? ").lower()
if answer == "canada":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What's the name of the Krew's minecraft series on Funneh's channel? ").lower()
if answer == "yandere high school":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What game was Itsfunneh's first video? ").lower()
if answer == "minecraft":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " out of 6 questions correct!")