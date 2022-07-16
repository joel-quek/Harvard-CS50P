from datetime import date, datetime, time
import inflect, sys, re
#----------------------------------------------------------------------------------
def main():
    my_birthday= get_birthday()
    phrase = subtract(my_birthday)
    print(f"{phrase} minutes")
#----------------------------------------------------------------------------------
def get_birthday():
    try:
        my_birthday = input("Date of Birth: ")
        datetime.strptime(my_birthday, '%Y-%m-%d')
        return my_birthday
    except ValueError:
        sys.exit("Invalid date")
#    return my_birthday
#----------------------------------------------------------------------------------
def subtract(my_birthday):
    d1 = datetime.strptime(my_birthday, "%Y-%m-%d")

    d2 = datetime.combine(date.today(), time(00,00))

    delta = d2 - d1

    delta = str(delta).split(" ")
    delta = int(delta[0])*24*60

    phrase = inflect.engine().number_to_words(delta).capitalize()
    phrase = re.sub(r"\s+and\s+"," ", phrase) #REGEX!!!!
    return(phrase)

#----------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------
    # 1989-10-18
    # 2021-07-02