#Start
print ("Amount Due: 50")
coin = int(input ("Insert Coin: "))

cost = 50 - coin

while cost > 0:
    if coin == 25 or coin == 10 or coin == 5:
        print ("Amount Due: ", cost)
        coin = input ("Insert Coin: ")
        coin = int(coin)
        cost = cost - coin
    else:
        print ("Amount Due: 50")
        coin = input ("Insert Coin: ")
        coin = int(coin)

if cost==0:
    print ("Change owed: 0")
else:
    cost = (-1)*cost
    print("Change owed:", cost)