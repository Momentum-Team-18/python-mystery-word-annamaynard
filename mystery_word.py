import random

def play_game(filename):
    with open(filename) as file:
        word_list = file.read().split()
        random_word = random.choice(word_list)
    
    while ' ' in word or '-' in word:
        word = random.choice(word_list)
    
    return word 


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #letters in word 
    used_letters = set()#what users have guessed 

    user_letter = input("Guess a Letter.")
    if user_letter in alphabet - used_letters:
            used_letters.add(used_letters)
            if user_letter.remove(user_letter):
                 word.letters.remove(user_letter)
                 
    elif user_letter in used_letters:
            print("You have already guessed this character. Please try again")

    else:
        print("Not a valid guess.")


if __name__ == "__main__":
    play_game("test-word.txt")
