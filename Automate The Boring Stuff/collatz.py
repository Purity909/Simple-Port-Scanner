import random

def gen_random():
        rand = random.randint(1, 1000)
        if rand % 2 == 0:
            print(f"{rand} is an even number.")
            rand = rand / 2
            print(f"{rand} is the new number")
        elif rand % 2 == 1:
            print(f"{rand} is an odd number.")        
            rand = rand * 3 + 1
            print(f"{rand} is the new number.")
        else:
             print("fuck you")

def user_input():
        num = int(input("Type your number here: "))
        if num % 2 == 0:
            print(f"{num} is an even number.")
            num = num / 2
            print(f"{num} is the new number.")
        elif num % 2 == 1:
            print(f"{num} is an odd number.")
            num = num * 3 + 1
            print(f"{num} is the new number.")
        else:
            print("fuck you")

def main(ask):
        if ask == 1:
            gen_random()             
        elif ask == 2:
            user_input()  
        else:
            print("You need to enter a valid input, bru.")                
        
ask = int(input("Random number(1) or enter your own(2)?\n--"))
main(ask)

# This has gone to oblivion