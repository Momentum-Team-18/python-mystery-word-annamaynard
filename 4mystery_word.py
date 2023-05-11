import random 


def play_game(filename):
    with open(filename) as file:
        word_list = file.read().split()
        #reads file and makes it a list 
        random_word = random.choice(word_list)
    print(random_word)
    display = ''
    for word in random_word:
        display += ' _'
    print(display)

    fail_count = 3
    letters_guessed = ""
    wrong_letter_count = 0
    

    while fail_count > 0:
        guess = input("Guess a letter : ")
        letters_guessed = letters_guessed + guess

    for i, letter in enumerate(random_word):
        if letter in letters_guessed:
            display = display[:i*2] + f' {letter}' + display[i*2+2:]
    print(display)
        # for word in random_word:
        #     if word in letters_guessed:
        #         display += f' {word}'
        #     else:
        #         display += ' _'
        # print(display)

    if guess in random_word: 
        print("\n")
        print("Good Job! Keep Going!")
        print("Letters guessed :", (letters_guessed))
    else:
        fail_count -= 1
        print("\n")
        print("Nope! Guess again!")
        print("Letters guessed :", (letters_guessed))
        
    for letter in random_word:
        if letter in letters_guessed:    
            print(f"{letter}", end="")       
    else:
        print("\n")    
        print(" _", end="")   
        wrong_letter_count += 1
    
    if wrong_letter_count == 0:
        print("\n")
        print(f"Good Job! The word was {random_word}")
    else:
        print("\n")
        print("You are out of guesses! Try again!")
        

if __name__ == "__main__":
    play_game("test-word.txt")



# update display when correct letters are added
# if player looses "Try again! 
# GOOD JOB not working? 
# wrong letter count? 
# letters guessed style? can it have more space? or happen on the same line as the good job!  ? 