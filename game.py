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
    
def play(num, count, digits, code):

  guess = int(input("Guess the number:"))
  num_int = int(num)
  if (guess == num_int):
    print("Great! You guessed the number. You're a Mastermind!")
    again()
  else:
    #indices = [i for i, letter in enumerate(num) if num == guess]
    #for index in indices:
      #code[index] = guess
    # num = "".join(code)
    print (code)
    print(num)
    num_str = str(num)
    guess_str = str(guess)
    
    if " " not in num:
      for j in range(0, digits):
        print("j", j)
        #print (guess_str)
        tmp_code = []
        for i in range(0, len(guess_str)):
          print ("i", i)
          print ("compare" + num_str[j] + " " + guess_str[i])
          if (guess_str[i] == num_str[j]) and j == i:
              count += 1
              code[i] = "O" 
              num_list = list(num_str)
              num_list[j] = "Q"
              num_str = "".join(num_list)
              print ("num_str", num_str)
          elif (guess_str[i] == num_str[j]) and j!=i:
            if code[i] != "O":
              code[i] = "_"
              count += 1
          else:
            if code[i] == "X":
              code[i] = "X"
              count += 1
        print (code)
        final = []
        if len(tmp_code) == 0:
          tmp_code = code
        for c in range(0, 4):
          print(c)
          prv = tmp_code[c] 
          cur = code[c]
          if cur == "O":
            final.append("O")
          elif cur == "_":
            if prv != "O":
              final.append("_")
          else:
            final.append("X")
        print (final)
          
        tmp_code = final
        print ("best so far")
        print (tmp_code)
        play(num, count, digits, tmp_code)
          
  if guess == num:
        count+=1
        print("You've become a Mastermind!")
        print("It took you only", count, "tries.")

def instructions():
  print ("the game is simple, there is a number, you must guess it.")
  print("you will be told how many you got in the correct position with an O.")
  print ("you will be told how many you got wrong with an X.")
  print("you will be told how many are in the wrong position but in the number with an _.")
  print ("you however will not be told which digits are which.")
  print ("every 10 guesses you will be given the opption to give up.")
  print ("every 20 you will be given the option to to see the instructions again")
  print ("Are you ready to see if you are a mastermind?")

def num_check(num): 
  while num[0] == num[1] and num[0] == num[2] and num[0] == num [3]:
    while num[1] == num[2] and num[1] == num[3] and num[2] == num[3]:
      num = random.randrange(1000,9999)
      num = str(num)
      num_check(num)  
  else:
    return num


def main():
  instructions()
  print (" ")
  level = int(input("how hard do you want the game to be? Level 1, 2, 3, 4, or 5?"))
  if level == 1:
    print (" ")
    print ("your number is 3 digits long. None of the digits are the same number.")
    digits = 3
    num = random.randrange(100, 999)
    num = str(num)
    while num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
      num = random.randrange(100, 999)
      num = str(num)
    print (num)
    num = str(num)
    count = 0
    code = []
    for d in range(0, digits):
      code.append("X")
    play(num, count, digits, code)
    
  elif level == 2:
    print(" ")
    print ("your number is 4 digits long. None of the digits are the same number.")
    digits = 4
    num = random.randrange(1000, 9999)
    print (num)
    num = str(num)
    num_check(num)
    print (num)
    num = str(num)
    count = 0
    code = []
    for d in range(0, digits):
      code.append("X")
    play(num, count, digits, code)
    
  elif level == 3:
    print(" ")
    print ("your number is 4 digits long. None of the digits are the same number, but some of the digits could be spaces.")
    digits = 4
    num = random.randrange(1000, 9999)
    num = str(num)
    print (num)
    num_check(num)
    count = 0
    code = []
    for d in range(0, digits):
      code.append("X")
    play(num, count, digits, code)
    
  elif level == 4:
    print("")
    print ("your number is 4 digits long. Some of the digits may be the same number.")
    digits = 4
    num = random.randrange(1000, 9999)
    num = str(num)
    print (num) #remove
    count = 0
    code = []
    for d in range(0, digits):
      code.append("X")
    play(num, count, digits, code)
    
  elif level == 5:
    print("")
    print ("your number is 5 digits long. Some of the digits may be the same number.")
    digits = 5
    num = random.randrange(10000, 99999)
    print (num)
    num = str(num)
    count = 0
    code = []
    for d in range(0, digits):
      code.append("X")
    play(num, count, digits, code)

  else:
    print ("that is not a valid level")
    level = int(input("how hard do you want the game to be? Level 1, 2, 3, 4, or 5?"))

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

