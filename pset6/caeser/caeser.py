import sys
import string

def main():
    ciphertext = []
    if len(sys.argv) < 2:
        usage()
        exit(1)
    try:
        key = int(sys.argv[1])
    except:
        usage()
    plaintext = input("plaintext: ")
    for x in plaintext:
        if x.isalpha() and x.islower():
            x = lower(x, key)
            ciphertext.append(x)
        elif x.isalpha() and x.isupper():
            x = upper(x, key)
            ciphertext.append(x)
        else:
            ciphertext.append(x)
    print("ciphertext: " + ''.join(ciphertext))

def usage():
    print("usage: caesar <key>")

def lower(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def upper(plaintext, shift):
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)



if __name__ == "__main__":
    main()