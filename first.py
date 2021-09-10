class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        
    def balanceinquiry(self):
        print("Your balance is: $1000")

    def cashwithdrawal(self,amount):
        new_amount = 1000 - amount
        print("You withdrawed: " + str(amount) + " Your remaing balance is: " + str(new_amount))

def main():
    name = input("Hello Welcome to Atm! What's your name: ")
    print("Hi, " + name)
    cardnumber = input("Insert your card number: ")
    pin = input("Enter your pin: ")
    new_user = Atm(cardnumber, pin)

    print("Choose your activity: ")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    activity = int(input("Enter your activity choice: "))

    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity == 2):
        amt = int(input("Enter the amount: "))
        new_user.cashwithdrawal(amt)
    else:
        print("Enter a valid number!!!")

if __name__ == "__main__":
    main()
