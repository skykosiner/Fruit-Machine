from random import *
from time import *

print("Fruit Machine")

reel = ["cherry", "bell", "lemmon"]
amountOfTimes = int(0)

money = int(input("please enter money "))
money = money
looping = True
numberGoes = int(1)

while looping:
    # Get random item from reel array and store it in a variole
    reel1 = choice(reel)
    reel2 = choice(reel)
    reel3 = choice(reel)

    # Take one away from money variole
    money = money - 1
    # Add one to the amount of times user has had a go
    amountOfTimes = amountOfTimes + 1
    # Print the amount of goes you have had
    print("You have had (%d) attempts" % numberGoes)
    # Print the results
    print(reel1 + " "+reel2+" "+reel3)
    # Wait two seconds
    sleep(2)
    # Change the number of goes to plus one
    numberGoes = numberGoes + 1
    # Check if user has run out of money
    if money == 0:
        print("Sorry you have run out of money pay for more or play again later")
        looping = False
    # If user gets all three slots in the row
    if reel1 == reel2 and reel1 == reel3:
        print("Jackpot")
        sleep(2)
        print()
        print()
        looping = False
