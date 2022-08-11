import random

def main():
    x = get_level()

    qns = 10
    tries = 3
    score = 0

    while qns > 0:
        y = generate_integer(x)
        z = generate_integer(x)
        w = int(input(f"{y} + {z} = "))
        if w == y + z:
            score = score + 1
            qns = qns - 1
        elif w != y + z:
            qns = qns - 1
            while tries > 0 and w != y + z:
                print ("EEE")
                tries = tries - 1
                w = int(input(f"{y} + {z} = "))
                ans = y + z
            print (f"{y} + {z} = {ans}")
#            break

    print (f"Score: {score}")
# ---------------------------------------------------------------------------------------------
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
               break
            else:
                raise ValueError
        except ValueError:
            pass
    return n
# ----------------------------------------------------------------------------------------------
def generate_integer(level):
    randnum = 0
    if level == 1:
        randnum = int(random.randint(0,9))
    elif level == 2:
        randnum = int(random.randint(10, 99))
    elif level == 3:
        randnum = int(random.randint(100, 999))
    return randnum
# ----------------------------------------------------------------------------------------------
if __name__ == "__main__": #(This line for what sia? Bu it changes the output. Only gawd knows)
    main()
