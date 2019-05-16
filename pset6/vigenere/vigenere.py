import sys
import string

LOWERDICT = {chr(i+96):i for i in range(1,27)}
UPPERDICT = {chr(i+64):i for i in range(1,27)}#


def main():
    # creates an empty list for the rotated characters to go into
    ciphertext = []
    # if an argument/key is not provided print the usage and exit with error code 1
    if len(sys.argv) < 2:
        usage()
        exit(1)
    # take in the users plaintext
    plaintext = input("plaintext :")


def usage():
    print("usage: vigenere.py <key>")

if __name__ == "__main__":
    main()