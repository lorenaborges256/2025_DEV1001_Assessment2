# Notify Me Application

## Overview

This app will notify you by email when a product or more are back in stock.


To make it works it will check the stock level and sends an email to the customer who wants to be notified when the desire product will be back in stock.

First it will require the account login, or create account.
if your email is still on our data, your account won't be created, but it will request you to login.

Our App will show the user, our products list, and they need to choose one to see if there is stock available to proceed to place your order. This app won't allow the user to place an order, it will be a future development. 
If a product is out of stock, stock = 0, user will be asked if they allow us to use thier email to notify them when the product is back in stock, if yes the user email will be added on a list.
App will ask the user if they want to check other product stock. If Yes, it will open the same menu as before, if not user will be requested to exit program.
Here ends our User interface. Our user will finish their app interation when they end check the stock and exit app.


On background, read these as "time is passing and things are happening".

for app test propose the message: ("\n🔔 Checking stock updates...") will be showing on screen, but it is a backgound work, user should not see that.
Our app continue checking stock level. stock_monitor.py
When product is back in stock (manually I edit stock.txt) notifier.py will send one email, per product desired, to the client/user, informing that product is back in stock, so they can place their order.

If it is a valid email it will be sent, it is not a valid email error message will be shown.

How to test and make sure client/user will receive a Notify-me email:
- stock.txt should have "str,int" caractheristcs, one product per line. And before starts app edit stock.txt writing at least one of those products with zero stock, You can add as many products with its stock you want, it will be seing on menu after login or account creation.
- create a account with a valid email, so you will receive it saying your product is back in stock.


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
store name, email and product requested to be informed. And make sure there is only one request per product per client. When client login or create a account the notifications.json is reset.
## class StockChecker:
20250606 at this moment: it makes sure the stock.txt is a valid data file. Also check is user type only products from the list, if not it shows a error message.
## class StockMonitor
20250606 After user ends to check stock and exit app, stock_monitor starts check every 10 seconds (to give time to manually change stock.txt) if a product change its stock from 0 to a positive value. If yes and a user request to be notified about that product it triggers next class Notifier to send email to this user.
and it stops to monitor
## class Notifier:
Use import smtplib and from email.mime.text import MIMEText to send email to the user. with a Subject and email content.


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

use pip list to see all packages install in this app
Maybe here will have something about privice https://policies.python.org/pypi.org/Terms-of-Service/ 
