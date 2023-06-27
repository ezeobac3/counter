import random
print ("hello world")
mylist = ["doing", "happy", "washing", "drawing", "writing", "driving", "cooking", "solving", "painting", "eating", "sleeping",
          "typing", "reading", "buying", "running", "swimming", "diving", "plaiting", "harvesting"]

def play():
    lives = 15
    word_list = []
    chosen = random.choice(item)
    play_list = list(chosen)
    print("this chosen word has" + len.chosen + "number of characters")
    new_list = []
    myinput = input("guess a single letter of the chosen word...>>>" )
    if myinput in play_list:
        play_list.remove(myinput)
        print(new_list.append(myinput))
        input("guess another number...>>> ")
        lives = lives - 1
    else:
        print("your input wasn't a correct guess. Try again")
        input("guess another number...>>> ")
        lives = lives - 1

    if lives == 0:
        print("Too many incorrect guesses. You ran out of lives. Failed!")


    if len(new_list = len(play_list)):
        print("congrats! you got the word correctly. The word is " + chosen)









