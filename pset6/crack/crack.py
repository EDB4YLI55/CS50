import sys
import string
from crypt import crypt

# this creates a dictionary starting with a empty character containing lowercase and uppercase
DICT = ' ' + string.ascii_uppercase + string.ascii_lowercase


def main():
    # this just checks if there is hash present, if not prints the usage
    if len(sys.argv) < 2:
        usage()
    # takes the first 3 chars and makes it a salt
    salt = sys.argv[1][0:3]
    # takes everything from char 3 onwards as the hash
    hash = sys.argv[1][3::]
    # this is a loop to a max of 5 chars long, it brute forces the hash with all possible passwords
    id4 = 0
    while id4 < 53:
        id3 = 0
        while id3 < 53:
            id2 = 0
            while id2 < 53:
                id1 = 0
                while id1 < 53:
                    id0 = 0
                    while id0 < 53:
                        # the lstrip removes the empty chars at the start
                        password = (DICT[id4] + DICT[id3] + DICT[id2] + DICT[id1] + DICT[id0]).lstrip()
                        # if the password matches the hash then we can assume that is the password so print it.
                        if crypt(password, salt) == salt + hash:
                            print(password)
                            exit(0)
                        id0 = id0 + 1
                    id1 = id1 + 1
                id2 = id2 + 1
            id3 = id3 + 1
        id4 = id4 + 1
        
        
def usage():
    print("usage: python crack.py hash")
    exit(1)
    

if __name__ == "__main__":
    main()