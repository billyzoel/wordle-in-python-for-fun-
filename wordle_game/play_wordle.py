from wordle import Wordle
from wordle import LetterState
from wordle import Keyboard
from colorama import Fore
import random

def main():
    
    #game set up
    check_library()
    word = get_random_word()
    wordle = Wordle(word)
    
    keyrow1, keyrow2, keyrow3 = format_keyboard()


    #game operation
    while wordle.can_attempt:
        x = input("\nYour guess is: ")

        #guess error conditions 
        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Your guess must be {wordle.WORD_LENGTH} letters long!" + Fore.RESET)
            continue

        if not check_valid_word(x):
            print(Fore.RED + f"Your guess must be a valid dictionary word! (with no duplicate letters)" + Fore.RESET)
            continue

        #guess executed conditions
        wordle.attempt(x)
        lines, result = display_results(wordle)
        print(draw_border_around(lines))

        guess_keyboard_format(result, keyrow1, keyrow2, keyrow3)
        print_keyboard(keyrow1, keyrow2, keyrow3)


    if wordle.is_solved:
        print("You've solved the puzzle")
    else:
        print("You've failed to solve the puzzle! The word is " + word)



def display_results(wordle: Wordle):
    print()
    lines = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["-"] * wordle.WORD_LENGTH))

    return lines, result



def draw_border_around(lines: [str], size: int=9, pad: int=1):
    '''Draws border around the wordle (defaults at size 9 padding 1)'''
    content_length = size + pad * 2
    space = " " * pad
    output = ""
    top_border = "        ┌" + "─" * content_length + "┐" +"\n"
    output = output + top_border
    for line in lines:
        mid_border = "        │" + space + line + space + "│"
        output = output + mid_border + "\n"

    bottom_border = "        └" + "─" * content_length + "┘"
    output = output + bottom_border + "\n"

    return output



def convert_result_to_color(result: [LetterState]):
    result_with_color = []

    for letter in result:
        if letter.is_in_position == True:
            color = Fore.GREEN
        elif letter.is_in_word == True:
            color = Fore.YELLOW

        else:
            color = Fore.WHITE

        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)



def check_library():
    with open("word_bank_filtered.txt", "r") as library:
        for word in library:
            if (len(word) - 1) != Wordle.WORD_LENGTH:
                raise Exception("Mismatched word length in game setting" +
                       " and word bank! Run filter.py or change" +
                        " max word length in wordle.py!")
    
    library.close()
    pass



def check_valid_word(word):
    with open("word_bank_filtered.txt", "r") as library:
        for valid_word in library:
            valid_word = valid_word.rstrip()
            if word == valid_word:
                return True
            
    return False



def get_random_word():
    library = open("word_bank_filtered.txt", "r")
    content = library.readlines()
    rng = random.randint(0, len(content))
    word = content[rng].rstrip()
    word = word.upper()
    return word



def format_keyboard():
    keyboard_a = open("key_alphabet.txt")
    keyboard_alphabet = keyboard_a.readlines()
    keyboard_a.close()
    key_list = []
    for keys in keyboard_alphabet:
        keys = keys.strip()
        key_list.append(keys)

    row1_key = []
    row2_key = []
    row3_key = []
    i = 0
    while i < 10:
        row1_key.append(Keyboard(key_list[i]))
        i += 1

    while i > 9 and i < 19:
        row2_key.append(Keyboard(key_list[i]))
        i += 1

    while i > 18 and i < 26:
        row3_key.append(Keyboard(key_list[i]))
        i += 1

    return row1_key, row2_key, row3_key



def guess_keyboard_format(letterstate_list, row1, row2, row3):
    
    for letterstate in letterstate_list:
        for item1 in row1:
            if item1.letter.upper() == letterstate.character.upper():
                item1.is_used = True
                item1.is_in_word = letterstate.is_in_word
                item1.is_in_position = letterstate.is_in_position
                
            continue        

        for item2 in row2:
            if item2.letter.upper() == letterstate.character.upper():
                item2.is_used = True
                item2.is_in_word = letterstate.is_in_word
                item2.is_in_position = letterstate.is_in_position

            continue

        for item3 in row3:
            if item3.letter.upper() == letterstate.character.upper():
                item3.is_used = True
                item3.is_in_word = letterstate.is_in_word
                item3.is_in_position = letterstate.is_in_position    

            continue

    pass



def print_keyboard(row1, row2, row3):
    #printing the first row of keyboard
    print("┌─┐" * 10)
    for item1 in row1:
        print(item1, end="")
    print()
    print("└─┘" * 10)

    #printing the second row of keyboard
    print(" " + "┌─┐" * 9)
    print(" ", end="")
    for item2 in row2:
        print(item2, end="")
    print()
    print(" " + "└─┘" * 9)

    #printing the third row of keyboard
    print("    " +  "┌─┐" * 7)
    print("    ", end="")
    for item3 in row3:
        print(item3, end="")
    print()
    print("    " +  "└─┘" * 7)

    pass



if __name__ == "__main__":
    main()