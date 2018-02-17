#! /usr/bin/python
import urllib2
import random
import string
from random import randint

length = input('How long is the password? ')
print(length)

answer = "yes"

while(answer == "yes" or answer == "Yes"):

    number = randint(10, 99)
    length = length - 3


    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

    response = urllib2.urlopen(word_site)
    txt = response.read()
    WORDS = txt.splitlines()

    word = random.choice(WORDS)

    while(len(word) != length):
        word = random.choice(WORDS)

    symbols = ["!", "@", "#", "$", "/"]
    mySymbol = random.choice(symbols)

    password = word + str(mySymbol) + str(number)
    password = string.capwords(password)
    print(password)
    length = length + 3

    answer = raw_input("Generate new password? Yes/No ")

host = raw_input('What is the password for? ')
output = host + " ~ " + password
print(output)

file = open("testfile.txt","w")

file.write(output)

file.close()
