# CodeforEE551_by_IC

This code is for gathering data from tweeter. 
Code searches(listens tweeter) ITEM or more than one ITEM in:
stream.filter(track=['ITEM'])

It writes tweets to a csv file and saves it in same directory as the code.

If there is any error "on_error" function stops the stream. If this function is not implemented, it will loop indefinitely

I have used another file for practice as a module where I have put tweeter API keys as variables and main code calls keys.py

I have used pypi.org, tweepy.org for learning modules and implementing tweepy module in Python.

Coded in: Sublime text editor
O/S: 64 Bit Linux Mint Distro
Software: Python 2.x, 
Python Modules: tweepy, csv
