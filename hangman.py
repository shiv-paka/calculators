import random
print("Hangman?")
wrds=["hello","hi","hola","bonjour","annyeonghaseyo"]
ranPick=random.choice(wrds)
for i in range(len(ranPick)):
    print("",end=" _ ")
print()
for i in range(len(ranPick)):
    wrdInp=input('Guess a letter: ').lower().strip()
    if wrdInp in ranPick:
        print(wrdInp)
    else :
        print(f"Try again only {i-1} guesses left!")
        break
