def main():
    shef = convert()
    output = gauge (shef)
#    print(type(shef)) #produces an Integer
    print (output)

def convert(w = ""):
    while True:
        try:
            w = input("Fraction: ")
            x = w.split("/")[0]
            y = w.split("/")[1]
            if (x.isnumeric() == False) or (y.isnumeric() == False):
                raise(ValueError)
            elif int(x) > int(y):
                raise (ValueError)
            elif y == int("0") or y == "0":
                raise(ZeroDivisionError)
            else:
                decimal = int(x) / int(y)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except IndexError:
            pass
    percent=decimal*100
    percent2 = int(percent) #convert returns an int
    return percent2

def gauge(percentage):
    x = "0"
    if percentage >= 99 and percentage <= 100:
        x = "F"
        #print("F")
    elif percentage <= 1 and percentage >= 0:
        x = "E"
        #print("E")
    elif percentage < 99 and percentage > 1:
        x = str(percentage) + "%"
        #print(percentage,"%")
    return x #gauge returns a str

if __name__ == "__main__":
    main()
