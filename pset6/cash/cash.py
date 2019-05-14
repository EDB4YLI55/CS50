

def main():
    pounds = get_float()
    # this basically tests for values lower than 0 and then prompts for input again.
    while pounds <= 0:
        pounds = get_float()
    # this turns the values into pennies rather than pounds
    pennies_owed = pounds * 100
    print(pennies_owed)
    # this takes all the 25p's out of the change owed
    twentyfive = int(pennies_owed / 25)
    # this takes all of the 10p's out of the change owed after th 25's have been removed.
    tens = int((pennies_owed % 25) / 10)
    # this takes all the oif the 5p's out of the changed owed after th 25p's and 10p's have been removed
    fives = int(((pennies_owed % 25) % 10) / 5)
    # this is what is left over after all of the 25p's, 10p's and 5p's have been taken, meaning the remainer must be pennies.
    pennies = int(((pennies_owed % 25) % 10) % 5)
    
    # prints the count of coins
    print(twentyfive + tens + fives + pennies)
    
    
def get_float():
    try:
        p = float(input("Changed Owed: "))
    except:
        p = get_float()
    return p
    
    
if __name__ == "__main__":
    main()