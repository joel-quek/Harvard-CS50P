def main():
    shef = input("Input: ")
    shef2 = remove_vowels(shef)
    print("Output: ", shef2)


def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in word:
        if c in vowels:
            word = word.replace(c,"")
    return word

main()