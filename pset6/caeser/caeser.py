import sys
import string


def main():
    # creates an empty list for the rotated characters to go into
    ciphertext = []
    # if an argument/key is not provided print the usage and exit with error code 1
    if len(sys.argv) < 2:
        usage()
        exit(1)
    try:
        # take the argument and save it as the varaible 'key' if the key is above 26 take 26 away from it until it is under 26 to get the equivalent rotation value.
        key = int(sys.argv[1])
        while True:
            if key > 26:
                key = key - 26
            else:
                # when the key is under 26 break the loop
                break
    # any issues with this, for example the user enters a value that is not a integar then print the usage
    except:
        usage()
    # take in the users plaintext
    plaintext = input("plaintext: ")
    # break down the plaintext into single characeters and loop through each ascii character one by one
    for x in plaintext:
        # if the character is alphabetical and is lowercase then run the rotation function for lowercase characters
        if x.isalpha() and x.islower():
            x = lower(x, key)
            # this append the returned value to the empty list called ciphertext
            ciphertext.append(x)
        # if the character is alphabetical and is uppercase then run the rotation function for uppercase characters
        elif x.isalpha() and x.isupper():
            x = upper(x, key)
            # append the result of the uppercase roation to the list called ciphertext
            ciphertext.append(x)
        else:
            # if the character is not alhabetic for example a space, number or punctuation, do nothing with it just append it to the ciphertext list
            ciphertext.append(x)
    # join the entire list together to make words and print
    print("ciphertext: " + ''.join(ciphertext))


def usage():
    print("usage: caesar <key>")

# this function takes in the character and the key and rotates it by the key


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