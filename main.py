import random
print("Welcome to Hangman!")
words = ["friday", "key", "money", "food", "church", "gate", "internet"]
word = words[random.randrange(len(words))]
lives = 5 
letter=[]

while lives < 30:
    guess = input("Enter your letter: ")
    if word.__contains__(guess):
        print ("Wow you guessed correctly")
        letter.append(guess)
        if letter.__len__() == word.__len__():
            print("Congratulations!!!")
            break
    else:
        lives -= 1
        if lives == 0:
            print("GameOver!!!  The word was ->", word )
            break
        else:
            print("Ooops, you have", lives, "lives left, try again my dear.")