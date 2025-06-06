# Notify Me Application

## Overview

This app will is a stock level checker and it send an email to the customer who wants to be notified when the desire product will be back in stock.

First it will require the account login, or create account.
if your email is still on our data, your account won't be created, but it will request you to login.

Our App will show the user, our products list, and they need to choose one to see if there is stock available to proceed to place your order. This app won't allow the user to place an order, it will be a future development.
If a product is out of stock, stock = 0, user will be asked if they want to be notified when it is back in stock, if yes the user email will be added on a list. 
User will notified by email when product be back in stock.
Here end our User application. Our user will finish their app interation when they end check the stock and exit app.

On background:
for app test propose a message ("\n🔔 Checking stock updates...") will be showing on screen, but it is a backgound work, user should not see that.
Our app continue checking stock level. stock_monitor.py
When product is back in stock (manually I edit stock.txt) notifier.py will send one email, per product desired, informing our client that product is back in stock, so they can place thier order.

If it is a valid email it will be sent, it is not a valid email error message will be shown.


changes on stock is detect only to increase, 0 -> x after user write exit on program.






# Class
## class UserAuth:
store name and email on user.json to check if user already exist, if email is in database user needs to login and not create a account. Also check if email is a valid email.
VALID EMAIL:
- test.email@example.com
- user123@sub.domain.org
- name+alias@email.net
- firstname.lastname@email.co.uk

INVALID EMAILS
- plainaddress (Missing '@' and domain)
- @missingusername.com (No username before '@')
- username@.com (Domain name can't start with a dot)
- user@domain..com (Consecutive dots in domain are not allowed)

## class CustomerRequest:
store name, email and product requested to be informed. Ans make sure there is only one request per product per client. When client login or create a account the notifications.json is reset.
## class StockChecker:
20250606 at this moment: it makes sure the stock.txt is a valid data file. Also check is user type only products from the list, if not shows a error.
## class StockMonitor
20250606 After user ends to check stock and exit app, stock_monitor starts check every 10 seconds (to give time to manually change stock.txt) if a product change its stock from 0 to a positive value. If yes and a user request to be notified it trigger  the next class Notifier to send email to this user.
and it stops to monitor
## class Notifier:
Use import smtplib and from email.mime.text import MIMEText to send email to the user.


# functions
## print_header

# Libraries
## import logging
## import smtplib
## import cowsay
## import schedule
## import time
## import json
## import os
## import re
