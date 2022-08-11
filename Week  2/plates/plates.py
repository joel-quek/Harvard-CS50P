def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# valid =   Num at end not in middle. (STUCK HERE)
# done max 6 chars min 2 chars. at least 2 letters. First num cannot be Zero. No periods space or punc.
def is_valid(s):
    character_list = word_split(s)
    maxpos = int(character_list.index(max(character_list)))
    sublistalpha = [x for x in character_list if x.isalpha()]
    sublistnum = [x for x in character_list if x.isdigit()]
    if len(character_list) > 6 or len(character_list) < 2:
        return False
    elif not character_list[0].isalpha() or not character_list[1].isalpha():
        return False
    elif len(sublistnum) > 0 and sublistnum[0] == '0':
        return False
    elif "." in character_list or " " in character_list or "," in character_list or "!" in character_list:
        return False
    elif int(len(character_list)) == 5 and character_list[4].isalpha():
        return False
    else:
        return True

def word_split (x):
    character = ()
    y = [character for character in x]
    return y

main()

#        firstnum = sublistnum[0]
#        indexfirst=character_list.index(firstnum)
#        minusone = int(int(indexfirst)-1)
#        plusone = int(int(indexfirst)+1)
#        if character_list(minusone).isalpha() == True and character_list(plusone).isalpha() == True:
#            return False