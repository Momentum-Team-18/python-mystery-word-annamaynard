import random 


def play_game(filename):
    with open(filename) as file:
        word_list = file.read().split()
    easy_list = []
    med_list = [] 
    hard_list = []
    for word in word_list:
        if len(word) < 4:
            easy_list.append(word)
        elif 3 < len(word) < 7:
            med_list.append(word)
        else:
            hard_list.append(word)

    level = None       
    while level not in ["easy", "medium", "hard"]:
        level = input(" What difficulty level would you like? easy, medium or hard?").lower()
        if level == "easy":
            word_list = easy_list
        elif level == "medium":
            word_list = med_list
        elif level == "hard":
            word_list = hard_list
        else:
            print("Please choose easy, medium or hard.")
    
    random_word = random.choice(word_list).upper()
    print(random_word)
    display = ''
    for word in random_word:
        display += ' _'
    print("What is the secret word??")
    print("\n")

    fail_count = 3
    letters_guessed = ""

    while fail_count > 0:
        
        for i, letter in enumerate(random_word):
            if letter in letters_guessed:
                display = display[:i*2] + f' {letter}' + display[i*2+2:]
        print(display)
        print("\n")
        if "_" not in display:
            print("YOU WIN!")
            break
            
        guess = input("Guess a letter : ").upper()
        letters_guessed += guess

        if guess in random_word: 
            print("\n")
            print("Good Job! Keep Going!")
            print("Letters guessed :", (letters_guessed))
            print("\n")
            
        else:
            fail_count -= 1
            print("\n")
            print("Nope! Guess again!")
            print("Letters guessed :", (letters_guessed))
            print("\n")


        if fail_count == 0:
            print("\n")
            print(f"LOSER! The word was {random_word}")


if __name__ == "__main__":
    play_game("test-word.txt")
