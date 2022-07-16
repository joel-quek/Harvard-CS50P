decimal=0
percent=0

while True:
    try:
        w = input("Fraction: ")
        decimal = int(w.split("/")[0]) / int(w.split("/")[1])
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


percent=decimal*100

if decimal > 0.99 and decimal <= 1:
        print("F")
elif decimal < 0.01 and decimal >= 0:
        print("E")
elif decimal <=1 and decimal >= 0:
        print(percent,"%")
        #THE CODE WORKS!!!!!!!