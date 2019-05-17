import sys


def main():
    
    if len(sys.argv) != 2:
        print('usage: python bleep.py dictionary')
        exit(1)
    
    # this creates an empty list for the users sentence to be put in (each word is an item)
    inputs = []
    # this creates a list that we will feed out banned.txt file into
    banned = []
    # this creates another empty list that we will add our filtered sentence too before joining.
    filtered = []
    # this section opens the file in read mode.
    file = open(sys.argv[1], 'r')
    file = file.read()
    # this iterates over the file to save each word in the banned list.
    for x in file.split('\n'):
        banned.append(x)
    # this takes in the user input - this will be the message with potentially bad words in.
    string = input("What message would you like to censor?: ")
    # this does the same process as early, splits the user string into words and adds it to a list called inputs.
    for x in string.split(' '):
        inputs.append(x)
    # this then takes each word from the inputs list, and checks if it exists in the banned list, if it does it replaces it with a * the same length as the word.
    for x in inputs:
        if x.lower() in banned or x.upper() in banned:
            x = len(x)
            x = '*' * x
            filtered.append(x)
        else:
            filtered.append(x)
    # this joins the filter lists words with a space.
    print(' '.join(filtered))
       

if __name__ == "__main__":
    main()