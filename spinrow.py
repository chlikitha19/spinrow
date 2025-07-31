import random
def spinrow():
    symbols =["😒","😊","😁"]
    list =[]
    for x in range(0,3):
        list.append(random.choice(symbols))
    return list
def print_row(row):
    
    x=" | ".join(row)
    print("-------------")
    print(x)
    print("-------------")
def pay_out(row,bet):
    if row[0]==row[1]==row[2]:
        if row[1]=="😒":
            return bet*3
        elif row[1]=="😊":
            return bet*5
        elif row[1]=="😁":
            return bet*10
    return 0
    
def main():
    balance = 100
    print("---------------------------")
    print("Welcome to python slots:")
    print("Symbols :😒😊😁")
    print("---------------------------")
    while balance > 0:
        print(f"your balance is ₹{balance}")
        bet=int(input('enter your bet amount'))
        if balance <bet:
            
            print('you have insufficient balance')
        elif bet<=0:
            print("your bet amount should be greater than zero")

        else:
            balance-=bet
        row = spinrow()
        print(row)
        print("!spinning........") 
        print_row(row)
        payout =pay_out(row,bet)
        if payout > 0:
            print(f"your won the payout {payout}")
        else:
            print('your did not won the payout')
        balance = payout+balance
        playagain= input("do you wanna play again")
        if playagain != "y":
            break     
if __name__ == "__main__":
    main()