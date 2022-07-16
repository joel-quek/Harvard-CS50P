# Sieve of Eratosthenes
# ---------------------------------------------------------------
import math
# ---------------------------------------------------------------
def main():
    N = get_input()
    integer_list = create_integer_list(N)
    #print(integer_list)
    composite_list = the_sieve(integer_list, N)
    # print(composite_list) # test print output
    # code works until composite_list. The problem is with removing the composite list
    prime_list = remove_composite_list(integer_list, composite_list)
    print(prime_list)
# ---------------------------------------------------------------
def get_input():
    x = input("Input number: ")
    if int(x) < int(2):
        raise ValueError("Number must be greater than 1")
    else:
        return int(x)
# ---------------------------------------------------------------
def create_integer_list(x):
    integer_list = []
    for i in range(int(x)):
        integer_list.append(i)
    integer_list.append(x)
    integer_list.remove(0)
    integer_list.remove(1)
    return integer_list
# ---------------------------------------------------------------
def the_sieve(integer_list, N): # x is the list of integers. n is the input.
    floor_root = math.floor(math.sqrt(N)) # returns floor square root of N
    composite_list = []
    for i in range(int(floor_root)):
        for j in range(2, int(N)):
            if ((int(integer_list[i]))*int(j)) in integer_list:
                composite_list.append((int(integer_list[i]))*int(j))
    return composite_list
# ---------------------------------------------------------------
def remove_composite_list(list_long, list_composite):
    prime_list = []
    for i in list_composite:
        if i in list_long:
            list_long.remove(i)
    prime_list = list_long
    return prime_list
# ---------------------------------------------------------------
if __name__ == "__main__":
    main()
# ---------------------------------------------------------------