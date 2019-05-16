import sys
import string

LOWERDICT = {chr(i+96): i for i in range(1, 27)}
UPPERDICT = {chr(i+64): i for i in range(1, 27)}


def main():
    # creates an empty list for the rotated characters to go into
    ciphertext = []
    rotation = []
    tmp = []
    # if an argument/key is not provided print the usage and exit with error code 1
    if len(sys.argv) < 2:
        usage()
        exit(1)
    # take the argument and save it as variable 'key'
    key = str(sys.argv[1])
    # this converts the key to numbers for example a=0 and c=3 and z=26 and saves it in a list called rotation
    for x in key:
        if x.isalpha() and x.islower():
            x = LOWERDICT.get(x)
            rotation.append(x - 1)
        elif x.isalpha() and x.isupper():
            x = UPPERDICT.get(x)
            rotation.append(x - 1)
        else:
            usage()
            exit(1)
    # this is a bodge, just make the list longer by 100 times, so it makes sure we have enough of a list to rotate large sentences.
    rotation = rotation * 100
    # take in the users plaintext
    plaintext = input("plaintext: ")
    # gets the length of the plaintext
    l = len(plaintext)
    id = 0
    # for each char in plain text, if it is alpha then print the number to a tmp list, if it is special ignore - this preventation rotation during spaces.
    for x in plaintext:
        if id < l and x.isalpha():
            tmp.append(rotation[id])
            id = id + 1
        else:
            tmp.append(rotation[id])
    id = 0
    # for each char and key in plaintext and tmp, if its is lower, rotate by that key, if it is upper, rotation by that key, if it is special do nothing but append
    for x, k in zip(plaintext, tmp):
        if id < l and x.isalpha() and x.islower():
            x = lower(x, k)
            ciphertext.append(x)
            id = id + 1
        elif id < l and x.isalpha() and x.isupper():
            x = upper(x, k)
            ciphertext.append(x)
            id = id + 1
        else:
            ciphertext.append(x)
            id = id + 1
    # join the ciphertext list together and print
    print('ciphertext: ' + ''.join(ciphertext))            
            

def usage():
    print("usage: vigenere.py <key>")
    

def lower(char, key):
    # this creates a variable containing all the letters of the alphabet, the same as doing alphabet = "abcdefg...etc...""
    alphabet = string.ascii_lowercase
    # this just creates another variable containing the alphabet rotated by the key.
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    # this does the transation between the two.
    table = str.maketrans(alphabet, shifted_alphabet)
    # return the rotated character
    return char.translate(table)


def upper(char, key):
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, shifted_alphabet)
    return char.translate(table)  
    

if __name__ == "__main__":
    main()