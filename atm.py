"""
MINI ATM BOOTH — Python CLI version
Educational demo only. This is not connected to a real bank.
"""

from datetime import datetime

account = {
    "name": "saikat",
    "balance": 75000,
    "pin": "1111",
    "type": "savings account",
    "account_number": "**** **** 7271",
}

MAX_PIN_ATTEMPTS = 3
transactions = []


def read_amount():
    raw = input("Enter your amount: ").strip()
    try:
        amount = int(raw)
    except ValueError:
        print("Invalid amount. Please enter a whole number.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return amount


def record_transaction(kind, amount):
    transactions.insert(0, {
        "kind": kind,
        "amount": amount,
        "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
    })
    del transactions[10:]


def check_balance():
    print(f"\nAVAILABLE BALANCE: BDT {account['balance']:,}")


def deposit_money():
    amount = read_amount()
    if amount is None:
        return
    account["balance"] += amount
    record_transaction("Deposit", amount)
    print(f"Deposit successful: BDT {amount:,}")
    check_balance()


def withdraw_money():
    amount = read_amount()
    if amount is None:
        return
    if amount > account["balance"]:
        print("Insufficient balance.")
        return
    account["balance"] -= amount
    record_transaction("Withdrawal", amount)
    print(f"Please collect your cash: BDT {amount:,}")
    check_balance()


def account_details():
    print("\n--- ACCOUNT DETAILS ---")
    print("Account name:", account["name"])
    print("Account number:", account["account_number"])
    print("Account type:", account["type"].title())
    check_balance()


def mini_statement():
    print("\n--- MINI STATEMENT ---")
    if not transactions:
        print("No transactions in this session.")
        return
    for item in transactions[:5]:
        sign = "+" if item["kind"] == "Deposit" else "-"
        print(f"{item['time']} | {item['kind']}: {sign}BDT {item['amount']:,}")


def change_pin():
    current = input("Enter current PIN: ").strip()
    if current != account["pin"]:
        print("Incorrect current PIN.")
        return
    new_pin = input("Enter new 4-digit PIN: ").strip()
    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("PIN must be exactly 4 digits.")
        return
    confirm = input("Confirm new PIN: ").strip()
    if confirm != new_pin:
        print("PIN confirmation did not match.")
        return
    account["pin"] = new_pin
    print("PIN changed for this session.")


def run_atm():
    print("=" * 38)
    print("       MINI ATM BOOTH")
    print("=" * 38)
    authenticated = False

    for attempt in range(MAX_PIN_ATTEMPTS):
        pin = input("Enter your 4-digit PIN (demo PIN: 1111): ").strip()
        if pin == account["pin"]:
            authenticated = True
            break
        remaining = MAX_PIN_ATTEMPTS - attempt - 1
        print(f"Invalid PIN. Attempts left: {remaining}")

    if not authenticated:
        print("Access denied. Please try again later.")
        return

    while True:
        print("\n" + "-" * 38)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. Mini Statement")
        print("6. Change PIN")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            account_details()
        elif choice == "5":
            mini_statement()
        elif choice == "6":
            change_pin()
        elif choice == "7":
            print("Thank you for using Mini ATM Booth.")
            break
        else:
            print("Invalid choice. Select 1–7.")


if __name__ == "__main__":
    run_atm()
