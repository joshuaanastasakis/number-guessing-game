#Things i still need to do:  
#1. make the XO_ def code 
#2. make it have different challenge levels
#3. make it so that the XO_ def code can be used in the main code

import random

def again():
  again = input("Do you want to play again?")
  if again == "yes":
    main()
  if again == "no":
    print ("thanks for playing")

def play(input_num):
  ## create a copy of input number as a list
  num = list(input_num)

  length = len(num)

  ## use 'done' to break out of the loop if the number has been guessed correctly
  done = False

  ## count the number of guesses so far
  count = 0

  ## Set default progress
  progress = []
  for i in range(0,length):
    progress.append('X')

  ## Repeatedly ask for a guess until  it's correct
  while done!=True:
    ## add a new line to separate guesses
    print(" ")

    ## TODO ask the user if they want to give up or need instructions
    ## choose which depending on the number of guesses so far (count)
    ## - if they choose to give up: exit the loop using the 'break' keyword (similar to the correct guess part below)
    ## - if they need instrucctions: show instructions

    ## ask the user for their guess
    guess = input("Enter your guess:")

    ## add 1 to guess count
    count += 1

    ## if the length of the guess does not match the length of the number, restart the loop
    if len(guess)!=length:
      print("Your guess must be", length, ", digits long")
      continue

    ## if the guess is correct, break out of the loop
    ## comparing to input_num because we're removing digits that were already correctly guessed from 'num'
    if guess==input_num:
      done=True
      break;

    ## if the guess is not a valid number, restart the loop
    if not guess.isnumeric():
      print("You must enter a valid number")
      continue

    ## compare the guess to the number
    for i in range(0, length):
      for j in range(0, length):
        if i==j:
          if num[i]==guess[j]:
            progress[j]='0'
            num[i]=' '
        else:
          if num[i]==guess[j]:
            if progress[j]!='0':
              progress[j]='_'

    print('progress:\t ', ''.join(progress))
    # print('number:\t ', ''.join(num))


  if done:
    print("You guessed correctly!")
  else:
    print("You failed")


def instructions():
  print ("the game is simple, there is a number, you must guess it.")
  print("you will be told how many you got in the correct position with an O.")
  print ("you will be told how many you got wrong with an X.")
  print("you will be told how many are in the wrong position but in the number with an _.")
  print ("you however will not be told which digits are which.")
  print ("every 10 guesses you will be given the opption to give up.")
  print ("every 20 you will be given the option to to see the instructions again")
  print ("Are you ready to see if you are a mastermind?")


## INPUT:
## - target = the length of the digit list
## - unique_digits = if the digits in the number have to be all different (True) or can repeat (False)
## RETURN: list of random digits
def rand_list(length, unique_digits):
  ## create tmp list that'll hold the random digits
  tmp = []

  ## loop 'length' number of times, adding a add a random digit to the tmp list each time
  for i in range(0, length):
    
    ## create random digit
    rand = str(random.randrange(0,9))
                                                                   
    ## if the list can't have repeating digits and has at least 1 digit already
    if unique_digits and len(tmp)>0:

      ## if the rand digit is in the list already, generate a new one until it's not in the list
      while rand in tmp:
        rand = str(random.randrange(0,9))

    ## add the random number to the list
    tmp.append(rand)

  ## return the list of random digits
  return tmp


def main():
  instructions()
  print (" ")

  ## Create variables to use as arguments to generate the random number
  ## - digits: length of the random number
  ## - unique_digits: if the number cannot have repeating digits
  ## These will be updated once a valid level has been selected by the user
  digits = 0
  unique_digits = False

  level = int(input("how hard do you want the game to be? Level 1, 2, 3, 4, or 5?"))
  
  ## Loop until a level between 1 and 5 is selected
  while True:
    if level == 1:
      print (" ")
      print ("your number is 3 digits long. None of the digits are the same number.")
      
      ## Update the variables for this level
      digits = 3
      unique_digits = True

      ## break out of the loop
      break
      
    elif level == 2:
      print(" ")
      print ("your number is 4 digits long. None of the digits are the same number.")
      
      ## Update the variables for this level
      digits = 4
      unique_digits = True

      ## break out of the loop
      break
      
    elif level == 3:
      print(" ")
      print ("your number is 4 digits long. None of the digits are the same number, but some of the digits could be spaces.")
      
      ## Update the variables for this level
      digits = 4
      unique_digits = True

      ## break out of the loop
      break
      
    elif level == 4:
      print(" ")
      print ("your number is 4 digits long. Some of the digits may be the same number.")
      
      ## Update the variables for this level
      digits = 4
      unique_digits = False

      ## break out of the loop
      break
      
    elif level == 5:
      print(" ")
      print ("your number is 5 digits long. Some of the digits may be the same number.")
      
      ## Update the variables for this level
      digits = 5
      unique_digits = False

      ## break out of the loop
      break

    else:
      ## no valid level was entered
      print ("that is not a valid level")
      level = int(input("how hard do you want the game to be? Level 1, 2, 3, 4, or 5?"))

      ## after the level is entered by the user, the loop will restart

  ## once we have a valid level, we can generate the random number as a list of digits
  ## we'll use the updated digits and unique_digits variables as arguments
  rand = rand_list(digits, unique_digits)

  # print('rand:', rand)
  
  ## convert the digits list to a string
  num = ''.join(rand)

  # print('rand joined:', num)

  ## start the game
  play(num)


def repeat():
  repeat = input("Do you want to get the instructions again?")
  if repeat == "yes":
    instructions()
  if repeat == "no":
    print ("ok")

def give_up(num):
  give_up = input("Do you want to give up?")
  if give_up == "yes":
    print ("the number was", num)
    again()
  if give_up == "no":
    print ("ok")
    

main()

