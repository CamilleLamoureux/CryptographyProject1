#Cryptography Project
Made by Anaïs Depeau and Camille Lamoureux

##Description
The key in this algorithm is two disorderly alphabets called _keyLeft_ and _keyRight_.

With this algorithm, we will encode each letter one by one, following those steps :

###1. Ciphering the letter
Find the letter to cipher in _keyRight_ and pick the corresponding letter in _keyLeft_. This last one will be the cipher letter.
###2. Reordering _keyLeft_ :
   1. Do a circular permutation such as the cipher letter must be in the first position (with an index equal to 0)
   2. Remove the letter of index 1, memorize it and replace it for a moment by a blank
   3. Shift by one location to the left all the letters which indexes are between 2 and 13
   4. Insert in the blank the letter which have been memorized earlier
   
###3. Reordering _keyRight_:
   1. Do a circular permutation such as the plain letter must be in last position (cith an index equal to 25)
   2. Remove the letter of index 2, memorize it and replace it for a moment by a blank
   3. Shift by one location to the left all the letters which indexes are between 3 and 13
   4. Insert in the blank the letter which has been memorized earlier

##Example of use
In this example we will have at the beginning :

- keyLeft : OAJTFYLQXCMPEDNVSBRUKHGWIZ
- keyRight : EWKFTYIQXUHPMABCNJRLDZSGVO

We want to encode SWAY using this method.

1. S as an index of 22 in _keyRight_. We take the letter of index 22 in _keyLeft_ as cipher letter, which is G.
2. We reorder _keyLeft_ :
    - We do the circular permutation such as the letter G get an index of 0.
    
    ```keyLeft = GWIZOAJTFYLQXCMPEDNVSBRUKH```
   
    - We remove the W (index 1) and replace it with a blank.
    
    ```keyLeft = G_IZOAJTFYLQXCMPEDNVSBRUKH```
    - We shift by one location to the left the letters which indexes are between 2 and 13.
    
    ```keyLeft = GIZOAJTFYLQXC_MPEDNVSBRUKH```
    
    - We insert in the blank the W we removed earlier
    
    ```keyLeft = GIZOAJTFYLQXCWMPEDNVSBRUKH```
3. We reorder _keyRight_ :
    - We do a cricular permutation such as the letter S get an index of 25.
    
    ```keyRight : GVOEWKFTYIQXUHPMABCNJRLDZS```
    
    - We remove the O (index 2) and replace it by a blank
    
    ```keyRight : GV_EWKFTYIQXUHPMABCNJRLDZS```
    
    - We shift by one location to the left all the letters which indexes are between 3 and 13
    
    ```keyRight : GVEWKFTYIQXUH_PMABCNJRLDZS```
    
    - We insert in the blank the O we removed earlier
    
    ```keyRight : GVEWKFTYIQXUHOPMABCNJRLDZS```

If we repeat these steps for all the letters from "SWAY", we obtain "GOPJ" as the cipher text.


