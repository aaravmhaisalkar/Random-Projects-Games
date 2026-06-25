import os
import time
all_guessed_letters = []

word = 'Tennis'

word_as_list = list(word.lower().strip())

blank_list = ["_"] * len(word_as_list)

def convert_to_string(list_of_letters):
    string = ''
    
    for letter in list_of_letters:
        string += letter
        
    return string


while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Word:", convert_to_string(blank_list))
    print("Guessed:"," ".join(all_guessed_letters))

    letter = input("\nGuess a letter: ").lower().strip()
    
    if letter in all_guessed_letters:
        print("Already guessed.")
        time.sleep(.5)
        continue
        
        
    all_locations = [i for i, x in enumerate(word_as_list) if x == letter]
    
    for i in all_locations:
        blank_list[i] = letter
    
    all_guessed_letters.append(letter)
    
    if blank_list == word_as_list:
        print("You win! The word was", word)
        break
    
   
