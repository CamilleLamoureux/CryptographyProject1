from function import algorithm1,generateKey

print("Bienvenue dans le premier algorithme de cryptage ! \n"
      "Voulez-vous (1 or 2): \n"
      "\t 1- Cipher your own message\n"
      "\t 2- Decipher (you will not choose the message or the key)\n")

choice = int(input("Your choice : "))

# If we want to cipher
if choice = 1:
    cipher = False
    text = list(input("Your message : "))
    keyLeft = generateKey()
    keyRight = generateKey()
    algorithm1(text, keyLeft, keyRight, cipher)

# If we want to decipher
elif choice = 2:
    cipher = True
    text = list("PJMNEAJFCDJPMXVMTAQUARKNPZDMWOSEOLMQBGBZTGPTHUHYSOVDLXEYAPUYYNLKAWETEBMLAWBFFPDGVKGKUBTRYDJIVEACLBYVLOLRJROQCHMQHSILAKWJCNDLQSXBOMNKFXSFKDGVDLCWQYDNLH")
    keyLeft = list("ALZBHGUWIEFJCDYNMQRVKPTOXS")
    keyRight = list("TWXLPRDZMNUGSAQKJHEBCIFYVO")
    algorithm1(text, keyLeft, keyRight, cipher)

# If the user give another number
else:
    print("Please try again and make sure your input is 1 or 2.")

    