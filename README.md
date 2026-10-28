# Mini ATM Booth

This project contains both:
- `atm.py` — Python command-line version based on the uploaded ATM code, expanded with mini statement and change PIN.
- `index.html` — browser version designed to look like a physical ATM booth, with a screen, keypad, cash dispenser slot, balance, deposits, withdrawals, account details, mini statement, PIN change, and recent activity.

## Run the Python version
Requires Python 3:
```bash
python atm.py
```
Demo PIN: `1111`

## Launch the website with GitHub Pages
GitHub Pages serves static HTML/CSS/JavaScript. It **cannot execute Python directly**. The `index.html` is a browser-side implementation of the same ATM flow; the Python source remains included in `atm.py`.

1. Create a GitHub repository (or use an existing one).
2. Upload `index.html`, `atm.py`, and `README.md` to the repository root.
3. Go to **Settings → Pages**.
4. Select **Deploy from a branch**, branch `main`, folder `/ (root)`, then save.
5. Wait for the deployment to finish and open the URL shown in Settings → Pages.

## Demo features
- PIN login (default `1111`) with three failed attempts per page session
- Balance inquiry
- Deposit and withdrawal with input validation and insufficient-funds check
- Account details
- Mini statement and recent transaction list
- Change PIN
- Saves demo balance, PIN, and transaction history in the same browser using `localStorage`

## Security warning
Educational simulation only. No real banking API or account is connected. Client-side PIN checks and localStorage are not secure authentication or secure storage. Do not use real banking credentials or real financial data.
