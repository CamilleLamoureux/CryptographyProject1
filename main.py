from function import algorithm1,generateKey,convertLetters

print('Welcome ! ! \n'
      'You want to (1 or 2): \n'
      '\t 1- Cipher (random generated keys)\n'
      '\t 2- Decipher\n')

choice = int(input('Your choice : '))

# If we want to decipher
if choice == 2:
    cipher = False
    text = list(input('Your cipher text : \n'))
    keyLeft = list(input('Your Left Key (see ReadMe for more specifications) : \n'))
    keyRight = list(input('Your Right Key (see ReadMe for more specifications) : \n'))
    algorithm1(text, keyLeft, keyRight, cipher)

# If we want to cipher
elif choice == 1:
    cipher = True
    text = list(input('Your message : '))
    keyLeft = generateKey()
    keyRight = generateKey()
    algorithm1(text, keyLeft, keyRight, cipher)

# If the user give another number
else:
    print('Please try again and make sure your input is 1 or 2.')