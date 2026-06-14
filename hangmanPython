heal = 100
wordToGuess = []
realWord = "spanish"
isAlive = True

while isAlive:
    win = True
    
    for letter in realWord:
        if letter in wordToGuess:
            print(f"{letter}")
        else:
            print("-")
            win = False

    if win:
        print("you win")
        break		

    enteredWord = input("enter letter: ")
    wordToGuess.append(enteredWord)

    if enteredWord not in realWord:
        heal = heal - 25
        print(f"Wrong Letter! Remaining heal: {heal}")

    if heal <= 0:
        print("you died")
        isAlive = False
