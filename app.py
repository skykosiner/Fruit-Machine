from random import *
from time import *

reel = ["cherry", "bell", "lemmon"]

while True:
    reel1 = choice(reel)
    reel2 = choice(reel)
    reel3 = choice(reel)

    print(reel1 + " "+reel2+" " reel3)
    sleep(2)
    if reel == reel2 and reel == reel3:
        print("Jackpot")
        sleep(2)
        print()
        print()
