#Hangman Game. 14/1/2023
#Vaibhavi Singhania S6-C
'''Hangman Game
A word is chosen randomly and the user has to guess the word by guessing letters.
The user has 6 lives.
For every mistake, the user looses a life and the hangman begins to appear, piece by piece.
The puzzle has to be solved before the hangman dies.
'''
import random
Words=['hangman','phenomenon','illustrate','functional','contrast','occupy','integrate','deviate','consume','idol','computer','python','hello','summer','winter','spring','autumn','newspaper','house']
ans='Y'
while ans=='Y' or ans=='y':
    word=random.choice(Words)
    length=len(word)
    L=[]
    L1=[]
    BP=1
    for i in range(length):
        L.append(word[i])
        L1.append('_')
    print("Current word is :",L1)
    L2=L1.copy()
    while L!=L1 or BP!=7:
        letter=input("Enter the letter: ")
        letter1=letter.lower()
        for i in range(length):
            if (L[i]==letter1):
                L1[i]=letter1
        if L1==L2:
            print("Body part number ",BP," has been added")
            BP+=1
        else:
            print("Current word is :",L1)
        L2=L1.copy()
        if BP==7:
            break
        if L1==L:
            break
    if L==L1:
        print("You win!")
        print("The word is", word)
    if BP==7:
        print("You lost! Hangman died!!")
        print(" The word was", word)
    ans=input("Do you want to play again?(Y/N) ")
print("Thank You For Playing!!")
