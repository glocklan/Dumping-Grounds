import os
import sys
print("Rock Paper Scissors: Enter your move by typing in R, S or P.")
p1 = input("Player 1 name: ")
p2 = input("Player 2 name: ")
win = 0
while win != 1:
    a = input(f"{p1}'s turn: ")
    if a != "R" and a != "S" and a != "P":
        print("Invalid input.")
        continue
    b = input(f"{p2}'s turn: ")
    if b != "R" and b != "S" and b != "P":
        print("Invalid input.")
        continue
    if a == "R" and b == "S":
        print(f"{p1} wins!")
        break
    if a == "P" and b == "R":
        print(f"{p1} wins!")
        break
    if a == "S" and b == "P":
        print(f"{p1} wins!")
        break
    elif a == b:
        print("Draw! Try again.")
        break
    else:
        print(f"{p2} wins!")
        break
c = input("Play again? Y/N: ")
if c == "Y":
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    print("Thanks for playing!")
    exit(0)
