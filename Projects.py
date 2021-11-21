#  1     ***   QR Code generator  ***
'''
import qrcode
import image
qr = qrcode.QRCode(
  version= 15, #15 means the version of the qr code high the number the bigger the code image and complicated picture
  box_size= 10, #size of the box where qr code will be displayed
  border=5  #it is the white part of image -- border in all 4 sides with white color

)

data = "https://www.youtube.com/watch?v=kJQP7kiw5Fk"
#as i have given the path of my channel like the same way you can give anything
# if you don't want to redirect and create for normal text that write text in the quotes

qr.add_data(data)
qr.make(fit=True)
img= qr.make_image(fill="black",black_color = "white")
img.save("test.png")
'''


#  2     Number Guessing
'''
import random
def guess(x):
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input('Guess a number between 1 and {x} :' ))
    if guess < random_number:
      print('Sorry, guess again, Too low.')
    elif guess > random_number:
      print('Sorry,guess again, Too high.')
  print(f'Yay, congrats.You have guessed the number {random_number} correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low(L), or corrct (C)').lower()
        if feedback =='h':
            high = guess -1
        elif feedback =='l':
            low = guess + 1

    print(f'yay! The computer guessed your number, {guess}, correctly!')


guess(10)
'''


#  3      Countdown Timer
'''
import time

def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(timer,end="\r")
    time.sleep(1)
    t -=1

  print('Time Completed!')

t = input('Enter the time in seconds: ')

countdown(int(t))
'''
#  4 Password Generator
'''
import random
print('Welcome to Your Password Generator')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?0123456789'

number = input('Amount of password to generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nHere are your passwords:')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)
'''

#          diabetics prediction
'''
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import  mean_squared_error

diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_predicted))

print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)
'''

#             TEXT TO SPEECH 
'''
from gtts import gTTS 
import os
text = "HEllo guys."

language = 'en'

obj = gTTS(text = text, lang = language, slow = False)

obj.save("sample.mp3")

os.system("sample.mp3")
'''

#             TEXT TO SPEECH 
'''
from gtts import gTTS 
import os

abc = open('sam.txt')
text = abc.read()

language = 'en'

obj = gTTS(text = text, lang = language, slow = False)

obj.save("sample.mp3")

os.system("sample.mp3")
'''

#                              ***  GUESS THE WORD  ***
'''
from math import trunc
import random
# library that we use in order to choose on random words from a list of words

name = input("What is your name? ")
# Here the user is asked to enter the name first

print("Good Luck ! ",name)

words = ['rainbow','computer','science','programming','python','mathematics','player','condition','reverse','water','board','geeks']

# Function will choose one random word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here 
turns = 12

while turns > 0:

  # counts the number of times a user fails
  failed = 0

  # all characters from the input word taking at a time.
  for char in word:
    # comparing that character with the character in guesses
    if char in guesses:
      print(char)
    else:
      print("_")

      # for every failure 1 will be incremented in failure
      failed += 1

  if failed == 0:
    # user will win the game if failure is 0 and 'You win' will be given as output
    print("You Win")

    # this print the correct word
    print("The word is: ",word)
    break

  # if user has inputthe wrong alphabet then it will ask user ti enter anither alphabet
  guess = input("Guess a charater: ")

  # every input character will be stored in guesses
  guesses += guess

  # check input character in word
  if guess not in word:

    turns -=1

    # if the character doesn't match the word then "Wrong" will be given as output
    print("You have", + turns, "more guesses")

    if turns == 0:
      print("You Lose")'''


#              VOTING SYSTEM 
'''
# first we will take input of what nominww what we want to keep
nominee1 = input("Enter the name of 1st nominee: ")
nominee2 = input("Enter the name of 2st nominee: ")

# intially vole count for both must be 0
nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:

  if voter_id == []:   # to check when voter list is completed
    print("Voting session is over !!! ")

    if nm1_votes > nm2_votes:
      percent = (nm1_votes / no_of_voter) * 100
      print(nominee1,"has won the election with ",percent,"% of votes")
      break  # to get rid of infinite loop

    elif nm2_votes > nm1_votes:
      percent = (nm2_votes / no_of_voter) * 100
      print(nominee2,"has won the election with",percent,"% of votes")
      break
    
    else:
      print("Both have equal number of votes !!!!!   Government will decide who will rule")
      break


  voter = int(input("Enter your voter id : "))
  if voter in voter_id:
    print("You are a voter ")
    
    voter_id.remove(voter)  # we will remove so that again same voter can't vote
    
    print("------------------------------------")
    print("To give vote to ",nominee1,"Press 1 ")
    print("To give vote to ",nominee2,"Press 2 ")
    print("------------------------------------")
    vote = int(input("Enter yout precious vote : "))
    
    if vote == 1:
      nm1_votes += 1
      print(nominee1,"Thank you to give your important vote to them !! ")
    
    elif vote == 2:
      nm2_votes += 1
      print(nominee2,"Thank you to give your important vote to them !! ")
    
    elif vote > 2:
      print("Check your pressed key !! ")

    else:
      print("You are not a voter OR You have already voted")
'''
#               OTP Generator
'''
import random
print('Welcome to Your OTP(One Time Password) Generator')
chars = '0123456789'

number = input('Amount of OTP to generate: ')
number = int(number)

length = input('Input your OTP length: ')
length = int(length)

print('\nHere are your OTPs:')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)
'''

