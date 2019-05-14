

def main():
    ccNumber = userInput()
    # this is the logic that checks the lenght and states INVALID if number is to short/long.
    if len(ccNumber) != 13 and len(ccNumber) != 15 and len(ccNumber) != 16:
        print("INVALID")
        exit(0)
    # this section just check the validity using the logic from Luhn's algorithm
    ccValidity = checkValidity(ccNumber, len(ccNumber))
    # if the function ccValidity returns a '0' then it is considered valid, and will move on else print invalid
    if ccValidity == 0:
        ccCompany(ccNumber, len(ccNumber))
    else:
        print("INVALID")
        exit(0)
    exit(0)
    
    
def userInput():
    try:
        # this takes userinput, under a try statement, so if the input fails to convert to integer it asks again
        ccNumber = str(input("Enter Credit Card: "))
        validinput = int(ccNumber)
    except:
        ccNumber = userInput()
    return ccNumber
    
    
def checkValidity(ccNumber, ccLength):
    # this creates a varaible which I toggle between true and false to reach every other number
    algorithmn = False
    # this creates a set of empty lists which I add the numbers to to deal with later
    first = []
    second = []
    overflow = []
    ccCopy = ccNumber[::-1]
    for x in (ccCopy):
        # if the toggle is false then it reads the numnber and appends it to the first list
        if algorithmn == False:
            first.append(int(x))
            algorithmn = True
        # if the toggle is true then it reads the number multiplies it by two and adds it to the second list
        elif algorithmn == True:
            second.append(int(x) * 2)
            algorithmn = False
    # this is an ugly bit of code, splitting numbers larger than 10 into for example 12 becomes 1 and 2
    for x in second:
        if x >= 10:
            for j in str(x):
                overflow.append(int(j))
        else:
            overflow.append(int(x))
    result = (sum(overflow) + sum(first))
    if result % 10 == 0:
        return 0
    else:
        return 1
        
        
def ccCompany(ccNumber, ccLength):
    start = []
    id = 1
    # this splits the credit card number down to the first two digits
    for x in ccNumber:
        if id <= 2:
            start.append(x)
            id = id + 1
    x = int(''.join(start))
    # this just checks what the card starts with provided it pass validity checks early and gives you the company.
    if x == 34 or x == 37:
        print("AMEX")
    elif x == 51 or x == 52 or x == 53 or x == 54 or x == 55:
        print("MASTERCARD")
    elif round(x / 10) == 4:
        print("VISA")
    else:
        print("INVALID")
        
        
if __name__ == "__main__":
    main()