import random

#
#   This program tries to create the hangman game.
#

print("\t Enter individual letters. This is a hangman game. ")

country_list=["India", "USA", "Netherland", "Germany", "Japan", "China", "Sri Lanka",
              "United Kingdom", "Australlia", "South Africa", "Brazil", "Argentina",
              "Canada", "Bhutan", "Nepal", "Turkey", "Israel"]

random_country = random.choice(country_list)
leng=len(random_country)

#    print(leng)
#    print(random_country)

guess_word=[None]*leng
random_word=list(random_country.lower())

print(guess_word)
print(random_word)


while guess_word != random_word:

    # Enter a letter and check if that letter is in the random_word
    temp=str(input("Enter a letter: "))
    #print(temp)
    print(random_country.count(temp))

    print(guess_word)

    if temp in random_word:
#        print(range(random_country.count(temp)))
        for i in range( len(random_word) ):
            if random_word[i] == temp:
                guess_word[i]=random_word[i]

        print(guess_word)

    else:
        print("Sorry. Enter another letter.")

else:
    print(guess_word)
