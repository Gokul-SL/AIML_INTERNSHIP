account = {
    "pin": "123",
    "balance": 1000.0,
    "history": []
}

def check_balance():
    print(f"\n[BALANCE] Your current balance is: ${account['balance']:.2f}")

def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            account['balance'] += amount
            account['history'].append(f"Deposited: ${amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Please enter a valid number.")

def withdraw():
    try:
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= account['balance']:
            account['balance'] -= amount
            account['history'].append(f"Withdrew: ${amount}")
            print("Withdrawal successful!")
        elif amount > account['balance']:
            print("Insufficient funds!")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Please enter a valid number.")

print("--- Welcome to Python ATM ---")
trial_pin = input("Enter your PIN: ")
if trial_pin == account['pin']:
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
           print("Goodbye!")
           break
        else:
            print("Invalid choice, try again.")
else:
    print("Wrong PIN. Access Denied.")
