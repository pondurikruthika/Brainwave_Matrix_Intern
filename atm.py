class ATM:
    def __init__(self, card_number, pin, balance=1000):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have successfully deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}. Your new balance is ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive number.")

def authenticate(card_number, pin):
    
    users = {
        "123456789": {"pin": "1234", "balance": 1000},
        "987654321": {"pin": "4321", "balance": 500},
    }

    if card_number in users and users[card_number]["pin"] == pin:
        print("Authentication successful!")
        return ATM(card_number, pin, users[card_number]["balance"])
    else:
        print("Invalid card number or PIN. Please try again.")
        return None

def main():
    print("Welcome to the ATM system.")
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")

    atm = authenticate(card_number, pin)

    if atm:
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Please choose an option (1-4): ")

            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                amount = float(input("Enter the amount to deposit: $"))
                atm.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: $"))
                atm.withdraw(amount)
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
