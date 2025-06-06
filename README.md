# Notify Me Application

## Overview

This app will is a stock level checker and it send an email to the customer who wants to be notified when the desire product will be back in stock.

First it will require the account login, or create account.
if your email is still on our data, your account won't be created, but it will request you to login.

It is a validation of email typed
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

Ourt App will show you our products list, and you need to choose one to see if there is stock available to proceed to place your order. This app won't allow you to palce your order, it will a future feature.
If any product is ourt of stock, you will be asked if you want to be notify, if yes your email will be added on a list. 
You will notified when product be back in stock.
Here end our User application. Our user will finish their app interation when they end check the stock and exit app.

On background:
for app test propose a message ("\n🔔 Checking stock updates...") will be showing on screen, but think about a backgound work, clint should not see that.
our app continue checking stock level.
When product is back on stock it will send one email informing our client that product is back in stock, so they can place thier order.

If it is a valid email it will be sent, it is not a error message will be shown.





# Class
## class CustomerRequest:
## class Notifier: 
## class StockChecker:

# functions
## print_header

# Libraries
## import smtplib
## import cowsay
## import schedule
## import time
## import json
## import os
## import re
