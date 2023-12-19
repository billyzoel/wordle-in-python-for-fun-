from wordle import Wordle
MAX_LETTER = Wordle.WORD_LENGTH

def main():
    
    output_file = open("word_bank_filtered.txt", "w")
    with open("word_bank.txt", "r") as input_file:
        for word in input_file:
            if filter_max_letter(word):
                if no_dup(word):
                    output_file.write(word)
    

    input_file.close()
    output_file.close()



def filter_max_letter(word):
    if len(word) != MAX_LETTER + 1:
        return False
    if len(word) == MAX_LETTER + 1:
        return True
    else:
        raise("Error in filtering max letter!")

def no_dup(word):
    word_list = []
    for letter in word:
        if letter not in word_list:
            word_list.append(letter)
        elif letter in word_list:
            return False
        
    return True


if __name__ == "__main__":
    main()
