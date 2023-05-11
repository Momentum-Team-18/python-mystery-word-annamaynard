import random

def play_game(filename):
    def valid_word(words):
        with open(filename) as file:
            word_list = file.read().split()
            random_word = random.choice(word_list)
        while '-' in word or ' ' in word: 
                word = random.choice(word_list)


    
    # word_completion = ' _' * len(word)
    guessed = False
    guessed_letters = []
    tries = 1 

    print('\n')
    print('Play a word guessing game!')
    print('\n')
    print(random_word)
    display = ''
    for word in random_word:
        display += ' _'
    print(display)

    while not guessed and tries > 0:
        guess = input('Please guess a letter.')
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter.")
            elif guess not in word: 
                print(guess, "is not in the word.")
                tries -= 1 
                guessed_letters.apend(guess)
            else: 
                print("Good job! This letter is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion) 
                indices = [i for i, letter in enumerate(word) if letter == guess]
                word_as_list[index] = guess
                word_completion = "".join and guess.isalpha()
                if "_" not in word_completion:
                    guessed = True    
  
            
        else:
            guesses -= 1
            print('nope')
            
    print("game over")








if __name__ == "__main__":
    play_game("test-word.txt")
