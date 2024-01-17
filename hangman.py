import random

def play_hangman():
    words = ['REJECT','ACTIVE','ACTUAL','CHARGE'] #initialized only 4 words
    word = words[random.randint(0,len(words))]
    lives = 5
    word_list = list(word)
    final_word = "-"*len(word)
    final_word_list = list(final_word)
    used_words_list = []

    while final_word != word:
        input_alphabet = input('Guess the alphabet. It is a {} letter word: '.format(len(word)))
        input_alphabet = input_alphabet.upper()
        if not input_alphabet.isalpha():
            print('Please select alphabet')
            continue

        if input_alphabet in word_list:
            indexes = [index for index, char in enumerate(word_list) if char == input_alphabet]
            if len(indexes) == 1:
                final_word_list[indexes[0]] = input_alphabet
            else:
                for index in indexes:    
                    final_word_list[index] = input_alphabet
        else:
            print('Your letter, {} is not in the word.'.format(input_alphabet))
            lives -= 1
        used_words_list.append(input_alphabet)
        print("You have {} lives and you have used these letters: ".format(lives), end = " ")
        print(*used_words_list)
        print("Current Word: ", end = " ")
        print(*final_word_list)
        final_word = ''.join(final_word_list)

        if not lives:
            print('Oh No! You lost the game. The Correct Word is {}'.format(word))
            break
    else:
        print('Hurray! You found the word!')

play_hangman()