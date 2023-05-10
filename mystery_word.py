import random

def play_game(filename):
    with open(filename) as file:
        word_list = file.read().split()
        random_word = random.choice(word_list)
    print(random_word)
    display = ''
    for word in random_word:
        display += ' _'
    print(display)

    word_list= {}
#  how do we display random word in dict or list 
#  how do we break that word down and assign key and values 



    guesses = 3
    while guesses > 0:
        letter = input("guess a letter: ")
        if letter in random_word:
            print('correct')
            
        else:
            guesses -= 1
            print('nope')
            
    print("game over")








if __name__ == "__main__":
    play_game("test-word.txt")
