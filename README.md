# Mini ATM Booth

A small ATM simulator built with Python and a browser-based interface. It supports basic account actions such as checking the balance, depositing money, withdrawing cash, viewing account details, and checking recent transactions.

## Features

- PIN-based access
- Balance inquiry
- Deposit and withdrawal
- Validation for invalid amounts and insufficient funds
- Account details
- Mini statement and recent transaction history
- Change PIN
- ATM-style web interface with a numeric keypad and cash dispenser design

## Account Details

- **Account holder:** Saikat
- **Account number:** `**** **** 7271`
- **Account type:** Savings account
- **Starting balance:** BDT 75,000
- **Demo PIN:** `1111`

These are sample details for this project only. Do not use real banking credentials.

## Project Files

- `atm.py` — command-line version of the ATM program.
- `index.html` — browser interface built with HTML, CSS, and JavaScript.

## Run the Python Program

Make sure Python 3 is installed, then run:

```bash
python atm.py
```

Enter the demo PIN `1111` when prompted. Follow the menu to check the balance, deposit or withdraw money, view account details, or exit.

## Run the Web Version

Open `index.html` in a modern browser. No package installation or build step is required.

The web version stores demo account activity in the browser's local storage, so it may remain available when you reopen the page in the same browser. Clearing browser data will remove that saved demo state.

## Deploy on GitHub Pages

GitHub Pages hosts static website files; it does not run Python code on its server. To publish the web interface:

1. Upload `index.html` to the root of your GitHub repository.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Choose the `main` branch and the `/(root)` folder, then save.
5. Open the published URL shown on the Pages settings screen.

Keep `atm.py` in the repository if you want others to view or run the Python version separately.

## Note

This project is for learning and demonstration. It is not connected to a bank, and it should not be used for real financial transactions. The PIN check and browser storage are not secure enough for a real banking application.

## Author

**Saikat**  
GitHub: [saikat-71](https://github.com/saikat-71)
