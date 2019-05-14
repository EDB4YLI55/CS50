def main():
    #gets user input
    h = height()
    #checks user input is within valid range, if not re-prompts
    while h < 1 or h > 8:
        h = height()
    #set spaces value
    s = int(h - 1)
    #for loop to increase printed hashes to max of height
    x = 1
    while x <= h:
        #calls the space function with the amount of spaces
        spaces(s)
        #calls the hash function with the amount of hashes
        hashes(x)
        x = x + 1
        #reduces the space count
        s = s - 1

def hashes(h):
    x = 0
    while x < h:
        print("#", end="")
        x = x + 1
    print()

def spaces(s):
    x = 0
    while x < s:
        print(" ", end="")
        x = x + 1

def height():
    try:
        h = int(input("Height: "))
    except:
        h = height()
    return h
    

if __name__ == "__main__":
    main()