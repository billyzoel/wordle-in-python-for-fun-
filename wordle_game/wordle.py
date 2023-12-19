from colorama import Fore

class Keyboard:
    def __init__(self, letter:str):
        self.letter: str = letter
        self.is_used: bool = False
        self.is_in_word: bool = False
        self.is_in_position: bool = False

    def __str__(self) -> str:
        if self.is_used == True and  self.is_in_word == False and self.is_in_position == False: 
            return (str("│" + Fore.RED + self.letter + Fore.RESET + "│"))

        if self.is_used == True and self.is_in_word == True and self.is_in_position == False: 
            return (str("│" + Fore.YELLOW + self.letter + Fore.RESET + "│"))
        
        if self.is_used == True and self.is_in_position == True and self.is_in_word == True:
            return (str("│" + Fore.GREEN + self.letter + Fore.RESET + "│"))
        
        else:
            return (str("│" + self.letter + "│"))


class LetterState:

    def __init__(self, character: str):
        self.character: str = character
        self.is_in_word: bool = False
        self.is_in_position: bool = False
        pass

    def __repr__(self) -> str:
        inword = "inword - " + str(self.is_in_word)
        inpos = "inpos - " + str(self.is_in_position)
        return self.character + ": " + inword + " " + inpos
        #print(*object, sep="\n") in main for clean output

class Wordle:
    
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    
    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
        return None
    
    def guess(self, word: str):
        word = word.upper()
        result = []

        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = (character == self.secret[i])
            result.append(letter)

        return result

    @property #able to call function like a variable
    def is_solved(self):
        return len(self.attempts) > 0 and (self.attempts[-1] == self.secret)

    @property
    def remaining_attempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return (self.remaining_attempts > 0 and not self.is_solved) 
    

