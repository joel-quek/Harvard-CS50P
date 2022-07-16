def main():
    shef = input("What time is it? ")
    shef2 = convert(shef)
    shef3 = change_to_float(shef2)
    if 7 <= shef3 and shef3 <= 8:
        print ("breakfast time")
    elif 12 <= shef3 and shef3 <= 13:
        print ("lunch time")
    elif 18 <= shef3 and shef3 <= 19:
        print ("dinner time")
    else:
        None
# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
# convert converts "7:30" to 7.5
def convert(t):
    h, m = t.split(":")
    h2 = change_to_float(h)
    m2 = change_to_float(m)
    m3 = m2 / 60
    t2 = h2 + m3
    round (t2, 2)
    change_to_float(t2)
    return t2
    # print(t2) this works

def change_to_float(f):
    return float(f)

#if __name__ == "__main__":
main()