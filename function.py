#Imports
import math


# Function that uppercase the plain text and remove spaces
def convertLetters(text):
    print("Convert Letters")


# Function that generate a key
def generateKey():
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    key = []
    for i in range(0,25):
        indexLetter = randint(0,len(abc))
        letter = abc[indexLetter]
        key.append(letter)
        abc.remove(letter)
    return key


# Function that verify the generated key
def keyOK(key):
    print("key OK")


# Function that reorder keyleft
def shifLeft(keyLeft,i):
    print("shiftLeft")


# Function that reorder keyRight
def shiftRight(keyRight,i):
    newKeyRight = []

    for letter in keyRight[i + 1:]:
        newKeyRight.append(letter)

    for letter in keyRight[:i + 1]:
        newKeyRight.append(letter)

    letterOfIndexTwo = newKeyRight[2]
    newKeyRight[2] = " "

    for letter in newKeyRight[3:14]:
        indexOfLetter = newKeyRight.index(letter)
        newKeyRight[indexOfLetter - 1] = letter

    newKeyRight[13] = letterOfIndexTwo

    return newKeyRight


# Function that cipher or decipher the given text
def algorithm1(text,keyLeft,keyRight,cipher):
    print("algorithm1")