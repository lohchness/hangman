# hangman
Simple hangman game

You have 6 chances to guess all the correct letters of a random word. Play the game by inputting 1 letter at a time, and you win when you guess all the correct letters.

# Running the script

```
python game.py
```

# Known bugs

The game breaks if you type in multiple letters at a time, and those multiple letters match a substring in the given word. Ex: typing in "all" when the word is "alligator". For this reason, players are urged to only type in 1 letter at a time. However, if the multiple letters do not match a substring in the given word, the game will continue as normal.
