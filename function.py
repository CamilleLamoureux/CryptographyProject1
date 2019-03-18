#Imports
from random import randint
import string

# Function that test if their are remaining spaces in the text
def noSpaceRemaining(text):
    return True if text.count(' ') == 0 else False


# Function that remove a space
def removeSpaces(text):
    while not noSpaceRemaining(text):
        text.remove(' ')


# Function that convert accent-letters to non-accent-letters
def removeAccents(text):
    accentsE = ['é', 'ẹ', 'è', 'ẻ', 'ẽ', 'ê', 'ế', 'ệ', 'ề', 'ể', 'ễ','ë']
    accentsA = ['á', 'ạ', 'à', 'ả', 'ã', 'ă', 'ắ', 'ặ', 'ằ', 'ẳ', 'ẵ', 'â', 'ấ', 'ậ', 'ầ', 'ẩ', 'ẫ','ä']
    accentsU = ['ú', 'ụ', 'ù', 'ủ', 'ũ', 'ư', 'ứ', 'ự', 'ừ', 'ử', 'ữ','ü']
    accentsI = ['í', 'ị', 'ì', 'ỉ', 'ĩ','ï']
    accentsY = ['ý', 'ỵ', 'ỳ', 'ỷ', 'ỹ','ÿ']
    accentsO = ['ó', 'ọ', 'ò', 'ỏ', 'õ', 'ô', 'ố', 'ộ', 'ồ', 'ỗ', 'ơ', 'ớ', 'ợ', 'ờ', 'ở', 'ỡ','ö']

    for i in range(len(text)):
        if text[i] == 'ç':
            text[i] = 'C'
        elif text[i] in accentsA:
            text[i] = 'A'
        elif text[i] in accentsE:
            text[i] = 'E'
        elif text[i] in accentsU:
            text[i] = 'U'
        elif text[i] in accentsI:
            text[i] = 'I'
        elif text[i] in accentsO:
            text[i] = 'O'
        elif text[i] in accentsY:
            text[i] = 'Y'


# Function that upper the text
def upper(text):
    for i in range(len(text)):
        text[i] = text[i].upper()

# Function that test if there is still punctuation signs
def noPuncSignRemaining(text):
    punctSigns = [',', '.', '?', '!', "'", '-', '_', ':', ';']
    for letter in text :
        if letter in punctSigns:
            return False
    return True

# Function that remove punctuations signs
def removePunctuationSigns(text):
    punctSigns = [',','.','?','!',"'",'-','_',':',';']
    while not noPuncSignRemaining(text):
        for element in punctSigns:
            if element in text :
                text.remove(element)


# Function that convert the givent text into a
def convertLetters(text):
    removeSpaces(text)
    removeAccents(text)
    removePunctuationSigns(text)
    upper(text)
    return text


# Function that generate a key
def generateKey():
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key = []
    for i in range(0,26):
        indexLetter = randint(0,len(abc)-1)
        letter = abc[indexLetter]
        key.append(letter)
        abc.remove(letter)
    return key


# Function that verify the generated key
def keyOK(key):
   if len(set(key).intersection(string.ascii_uppercase))==26:
       return True
   return False



# Function that reorder keyleft
keyLeft = ['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'Q', 'W', 'X',
           'C', 'V', 'B', 'N']
valeur = str("R")
i = keyLeft.index(valeur)

def shiftLeft(keyLeft, i):
    newkeyLeft = []

    for lettre in keyLeft[i + 1:]:
        newkeyLeft.append(lettre)

    for lettre in keyLeft[:i ]:
        newkeyLeft.append(lettre)

    print(newkeyLeft)

    newkeyLeft.insert(0, valeur)

    print(newkeyLeft)

    position1 = newkeyLeft[1]
    newkeyLeft[1] = ' '
    print(newkeyLeft)

#partie de test, non finie, cause des erreurs affichées
    for lettre in newkeyLeft[2:13]:
        deplacement = newkeyLeft.index(lettre)
        deplacement-=1

    print(newkeyLeft)

    print('shiftLeft')

    newkeyLeft[13] = position1
    print(newkeyLeft)


# Function that reorder keyRight
def shiftRight(keyRight,i):
    newKeyRight = []

    for letter in keyRight[i + 1:]:
        newKeyRight.append(letter)

    for letter in keyRight[:i + 1]:
        newKeyRight.append(letter)

    letterOfIndexTwo = newKeyRight[2]
    newKeyRight[2] = ' '

    for letter in newKeyRight[3:14]:
        indexOfLetter = newKeyRight.index(letter)
        newKeyRight[indexOfLetter - 1] = letter

    newKeyRight[13] = letterOfIndexTwo

    return newKeyRight


# Function that cipher or decipher the given text
def algorithm1(text,keyLeft,keyRight,cipher):
    pass
