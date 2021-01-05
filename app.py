from random import *
from time import *

print("Fruit Machine")

reel = ["cherry", "bell", "lemmon"]
amountOfTimes = int(0)

money = int(input("please enter money "))
money = money
looping = True
numberGoes = int(0)

while looping:
    reel1 = choice(reel)
    reel2 = choice(reel)
    reel3 = choice(reel)

    money = money - 1
    amountOfTimes = amountOfTimes + 1
    print("You have had (%d) attempts" % numberGoes)
    print(amountOfTimes)
    print(money)
    print(reel1 + " "+reel2+" "+reel3)
    sleep(2)
    # Change the number of goes to plus one
    numberGoes = numberGoes + 1
    # Check if user has run out of money
    if money == 1:
        print("Sorry you have run out of money pay for more or play again later")
        looping = False

    if reel1 == reel2 and reel1 == reel3:
        print("Jackpot")
        sleep(2)
        print()
        print()
        looping = False
