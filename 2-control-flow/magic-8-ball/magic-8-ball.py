# Magic 8-Ball 🎱
# Loren Hartman

import random

name = ""
question = ""
answer = ""

random_number = random.randint(1, 9)
# print(random_number)

if question.strip() == "":
  print("You need to ask a question first!")
else:
  if name == "":
    print("Question: " + question)
  else:
    print(name + " asks: " + question)

  
if question != "":
  if random_number == 1:
    answer = "Yes - definitely"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 2:
    answer = "It is decidedly so"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 3:
    answer = "Without a doubt"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 4:
    answer = "Reply hazy, try again"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 5:
    answer = "Ask again later"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 6:
    answer = "Better not tell you now"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 7:
    answer = "My sources say no"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 8:
    answer = "Outlook not so good"
    print("Magic 8-Ball's answer: " + answer)
  elif random_number == 9:
    answer = "Very doubtful"
    print("Magic 8-Ball's answer: " + answer)
  else:
    answer = "Error"

# print("Magic 8-Ball's answer: " + answer)
