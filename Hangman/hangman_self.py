import random
from words import choose_word
from images import IMAGES

'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    
    '''
    secret_word: word to be guessed by the user
    letters_guessed: list holds all the words guessed by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    secret_word = sorted(list(set(secret_word)))
    letters_guessed = sorted(letters_guessed)

    temp = True
    for x in secret_word:
        if x in letters_guessed:
            pass
        else:
            temp = False

    return temp

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    
    '''
    secret_word: word to be guessed by the user
    letters_guessed: list holds all the words guessed by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    
    index = 0
    guessed_word = ""
    
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
    


def get_available_letters(letters_guessed):
    
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    # all_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # all_letters_copy = all_letters
    
    # for char in letters_guessed:
    #     if char in all_letters:
    #         all_letters.remove(char)
    #     else:
    #         continue
            
    # letters_left = all_letters
    # all_letters = all_letters_copy
    
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters = set(all_letters)
    
    letters_guessed = set(letters_guessed)
    
    letters_left = sorted(list(all_letters - letters_guessed))
    
    letters_left = "".join(letters_left)
    return letters_left


def display_image(image_index):
    return IMAGES[image_index]


def hint(secret_word, letters_guessed):
    empty_array = []
    for char in secret_word:
        if (char not in letters_guessed):
            empty_array.append(char)
            
        
    random_char = random.choice(empty_array)
    
    return random_char
    

def hangman(secret_word):
    
    
    remaining_lives = 8
    hint_count = 1
    
    '''
    secret_word (string) : word to be guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    
    print("WELCOME TO THE GAME, HANGMAN !")
    print("I am thinking of a word that is {} letters long.".format(str(len(secret_word))), end='\n\n')
        
    letters_guessed = []

    while ((remaining_lives != 0) and (hint_count >= 0)):

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        
    
        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
            
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: {} ".format(available_letters))   
            
            if is_word_guessed(secret_word, letters_guessed):
                print(" * * CONGRATULATIONS, YOU WON !!! * * ", end='\n\n')
                print("VERY WELL PLAYED !!!")
                break   
            
            
        elif letter == "hint":
            hint_count -= 1
            letters_guessed.append(hint(secret_word, letters_guessed))
            
            print("HINT USED : {}".format(get_guessed_word(secret_word, letters_guessed)))
            
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: {} ".format(available_letters))   
            
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * CONGRATULATIONS, YOU WON !!! * * ", end='\n\n')
                print("VERY WELL PLAYED !!!")
                break
            
        else:
            print("Oops! That letter is not in my word: {} ".format(get_guessed_word(secret_word, letters_guessed)))
            
            letters_guessed.append(letter)
            print("")
            
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: {} ".format(available_letters)) 
            print("\n")
  
            print(display_image(8 - (remaining_lives)))
                               
            remaining_lives -= 1
            print("REMAINING LIVES :", remaining_lives)
            
            continue
        
       
    if (remaining_lives == 0):
        print("BETTER LUCK NEXT TIME ! :)")
        
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
