"""
Simple hangman example.
"""

# import the time
import time

# welcome the user
name = raw_input("What is your name? ")

print "Hello, ", name, "Time to play hangman!"

print "\n"

# wait for 1 second
time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

# set the secret
word = "secret"

# empty
guesses = ''

# turns
turns = 10

# while

# check if > 0
while turns > 0:
    # counter
    failed = 0
    # check word
    for char in word:

        # see
        if char in guesses:
            print char,
        else:
            print "-",
            failed += 1

    if failed == 0:
        print "\n", name, "you won!"

        # exit the script
        break

    print

    guess = raw_input("guess a character: ")

    guesses += guess

    if guess not in word:

        # decrease
        turns -= 1
        print "Wrong\n"
        print "You have", + turns, "guesses left."
        if turns == 0:
            print name, "you lose!\n"

# end
