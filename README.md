# Notify Me CLI Application

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-prototype-orange.svg)]()
[![Platform](https://img.shields.io/badge/platform-CLI-lightgrey.svg)]()
![Made with Cowsay](https://img.shields.io/badge/made%20with-cowsay-ff69b4?style=flat-square&logo=gnu&logoColor=white)

## Overview

The **Notify Me CLI Application** simulates a "Notify Me" feature commonly used in online stores. Users can register, browse available products, and request email notifications when out-of-stock items become available again.

This CLI tool is built for rapid testing and demonstrates the potential architecture and logic behind future live-inventory integrations with web platforms. Built as a prototype for future integration with e-commerce platforms.


## Features

- **User Account System**
  - Register with name and email (validated using RegEx)
  - Existing account lookup via `users.json`

- **Stock Interaction**
  - Add or delete products from `stock.txt`
  - View the current product list at any time
  - Manually update product stock

- **Email Notification**
  - Opt-in to receive email alerts when products are restocked
  - Emails sent using Gmail SMTP; credentials stored in `credentials.txt` (ignored by version control)

- **Session Monitoring**
  - Background stock monitor activates upon app exit
  - Ends when timeout occurs or product is back in stock
  - Logs refreshed per session via `sent_notifications.json`


## Developer Notes

- **Language:** Python 3.x  
- **Modules:** `re`, `json`, `os`, `time`, `smtplib`, `email.mime`: All standard Python library modules. 
- **Data Persistence:** Uses `.json` and `.txt` files for lightweight storage  
- **Security Notes:**  
  - `credentials.txt` contains plaintext Gmail login (should be secured in future versions)
  - Ensure `.gitignore` excludes sensitive files


## License

This project is licensed under the **MIT License**.
You're free to use, modify, and distribute this software with attribution. See the [`LICENSE`](LICENSE) file for details.
All standard Python library modules, such as `re`, `json`, `os`, `time`, `smtplib`, and `email.mime`, are upon of Python Software Foundation License (PSFL). Legal/Ethical Impact: Open source and permissive. You're free to use, modify, and distribute without restrictions. Ethically safe—commonly used in Python projects.

Files such as `users.json`, `notifications.json`, `sent_notifications.json`, and `credentials.txt`, may have personal data, it needs to comply with Australian Privacy Act or GDPR, especially regarding user consent and data handling. They should never be shared, due to privacy and security risks.

## Setup:
1. Get the Project Files – Download or clone the repository to your computer.
2. Open the Project Directory – Use the terminal to move into the project's folder:
```bash
cd path/to/project
```
3. Install Dependencies – Install all required packages listed in requirements.txt:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Only if you're developing
```
4. You are ready to start the Application 

## How to use - TESTING GUIDE

### 1. Manage Products Stock
- Add/Delete items in `stock.txt` with correct format BEFORE launch the App. 
- Make sure that at least one product has 0 (zero) units in stock, for notification test.
- Full stock list will be shown when App launched.


### 2. Launch App
```bash
python3 main.py
```
### 3. Register / Log In
- New users: enter your name and email
- Existing users: email is checked against users.json

### 4. Opt-In for Notifications
- Select products you want alerts for when restocked
- Answer if you give the app permission to use your email to send you a notification

### 5. Exit to Monitor
- Exit the App when finish your research
- On exit, the app runs a monitor script to check for stock updates
- Following the prompt, update manually products stock in `stock.txt` to trigger notifications.
- Emails will be sent

---

## Future Vision
In future versions, this app will:
- Integrate directly with e-commerce product inventory APIs
- Embed into live product pages with a "Notify Me" button
- Collect and sync customer profiles from the store database
- Monitor inventory in real-time and scale alerts across multiple products