import random

# even = divide by 2
# odd multiply by 3 and add 1
# repeat until the result = 1


def math(rand):
    while rand % 2 == 0 and rand > 1: # if 'rand' is even
        rand = rand / 2
        print(rand)

    while rand % 2 == 1 and rand >= 1: # if 'rand' is odd
        rand= (rand * 3) + 1
        print(rand)         

if __name__ == "__main__":
    rand = random.randint(1, 10000) # generate random number and store it
    print(f"Your number is {rand}.")
    math()         