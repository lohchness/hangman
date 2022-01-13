import string, os, random

alphabet_list = [i for i in string.ascii_lowercase]
available_themes = ["animals", "countries"]

WORD_UNDERLINE = "___"
WORD_SPACE = " "
STAGE_START = 0
UNDERLINED_BLANK = "\033[4m \033[0m"


def input_theme():
    os.system('cls')
    print("Available themes:\n1 - Animals\n2 - Countries\n") 
    theme = input("Enter the NUMBER corresponding to the name of the theme you want to play: ")
    game(theme) if theme.isnumeric() and int(theme) <= len(available_themes) else input_theme()

def game(theme):
    curr_stage = STAGE_START
    word = random.choice(list(open(f"{available_themes[int(theme)-1]}.txt"))).replace("\n", "")
    wrong_letters = []
    correct_letters = []
    used_letters = wrong_letters + correct_letters

    while True:
        print_hangman(curr_stage)
        construct_word(word, wrong_letters, correct_letters)
        
        new_letter = input("\nGuess a letter!: ")

        if new_letter in word:
            correct_letters.append(new_letter)
        else:
            wrong_letters.append(new_letter)
            curr_stage += 1

        without_space = word.replace(" ","")
        if set(correct_letters) == set(without_space):
            print_hangman(curr_stage)
            construct_word(word, wrong_letters, correct_letters)
            game_win(word)
        
        if len(wrong_letters) == 6:
            print_hangman(curr_stage)
            game_lose()
    

def print_hangman(stage):
    os.system('cls')
    hangman_head_0 = """\
    _________________________
     |                     |
     |
     |
     |"""
    hangman_head_1 = """\
    _________________________
     |                     |
     |                    _|_
     |                   |   |
     |                   |___|"""
    hangman_body_0 = """\
     |
     |
     |
     |
     |
     |"""
    hangman_body_1 = """\
     |                     |
     |                     |
     |                     |
     |                     |
     |                     |
     |                     |"""
    hangman_body_2 = """\
     |                     | 
     |                    /|
     |                   / |
     |                  /  |
     |                 /   |
     |                     |"""
    hangman_body_3 = """\
     |                     | 
     |                    /|\\
     |                   / | \\
     |                  /  |  \\
     |                 /   |   \\
     |                     |"""
    hangman_legs_0 = """\
     |
     |
     |
     |
     |
    |_|"""
    hangman_legs_1 = """\
     |                    /
     |                   /
     |                  /
     |                 /
     |                      
    |_|"""
    hangman_legs_2 = """\
     |                    / \\
     |                   /   \\
     |                  /     \\
     |                 /       \\
     |                      
    |_|"""
    if stage == 0:
        print(hangman_head_0, hangman_body_0, hangman_legs_0, sep='\n')
    elif stage == 1:
        print(hangman_head_1, hangman_body_0, hangman_legs_0, sep='\n')
    elif stage == 2:
        print(hangman_head_1, hangman_body_1, hangman_legs_0, sep ='\n')
    elif stage == 3:
        print(hangman_head_1, hangman_body_2, hangman_legs_0, sep ='\n')
    elif stage == 4:
        print(hangman_head_1, hangman_body_3, hangman_legs_0, sep ='\n')
    elif stage == 5:
        print(hangman_head_1, hangman_body_3, hangman_legs_1, sep ='\n')
        print("\nLAST LIFE, CHOOSE WISELY\n")
    elif stage == 6:
        print(hangman_head_1, hangman_body_3, hangman_legs_2, sep ='\n')
        game_lose()

def construct_word(word, wrong_letters, correct_letters):
    print("\n")

    # Wrong letters
    print("Wrong letters: ", end="")
    for i in wrong_letters:
        print(i.upper(), end=" ")
    print("\n")

    # Underlines where correct letters are revealed
    for letter in word:
        if letter == WORD_SPACE:
            print("   ", end="")
        else:
            print(UNDERLINED_BLANK, end="")
            if letter in correct_letters:
                print(f"\033[4m{letter.upper()}\033[0m", end="")
            else:
                print(UNDERLINED_BLANK, end="")
            print(UNDERLINED_BLANK, end=" ")
    print("\n")

def game_win(word):
    input("\nCongrats! You've guessed the correct word!. Press Enter to play again.")
    input_theme()

def game_lose():
    input("\nUh oh, you lost! Press Enter to play again.")
    input_theme()

if __name__ == "__main__":
    os.system("color") # Makes ANSI escape sequence get processed correctly
    
    input_theme()
