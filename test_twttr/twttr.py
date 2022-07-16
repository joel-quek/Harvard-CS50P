def main():
    shef = input("Input: ")
    shef2 = shorten(shef)
    print("Output: ", shef2)


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in word:
        if c in vowels:
            word = word.replace(c,"")
    return word

if __name__ == "__main__":
    main()