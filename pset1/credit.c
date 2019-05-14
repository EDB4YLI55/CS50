#include <stdio.h>
#include <cs50.h>
long int ccNumber;

//this function is for user to enter their credit card details
long int userInput() 
{
    ccNumber = get_long("Enter Credit Card: ");
    return ccNumber;
}
//this counts length, only 13, 15 and 16 numbers long are accepted, but I'll do that logic later
int checkLength(long int x)
{
    int l = 0;
    while(x != 0)
    {
        x = x/10;
        l ++;
    } 
// returns length
    return l;
}
//this section is Luhn's Algorithm - This shit was hard, like so fucking hard
int checkValidity(long int x, int l)
{
    int count = 0;
    bool algorithmn = false;
    int first = 0;
    int second = 0;
    int buff = 0;
    int result;
    while (count < l)
    {
        if (algorithmn == false)
        {
            first = first + (x % 10);
            x = x / 10;
            algorithmn = true;
            count++;
        }
        else if (algorithmn == true)
        {
            if (checkLength(x % 10 * 2) > 1)
            {
                second = x % 10 * 2;
                second = (second % 10) + (second % 20 / 10);
                buff = buff + second;
                x = x / 10;
                algorithmn = false;
                count++;
            }
            else
            {
                second = x % 10 * 2;
                buff = buff + second;
                x = x / 10;
                algorithmn = false;
                count++;
            }
        }
    }
    result = first + buff;
    if (result % 10 == 0)
    {
        //if number is valid against the algorithm then return a '0' for yes
        return 0;
    }
    else
    {
        //if number is not valid against the algorithmn then return a '1' for no
        return 1;
    }
}
void ccCompany(long int n, int l) 
{
    int i = n;
    int x;
    int c = 0;
    while (c < l)                //4003600000000014
    {
        i = n % 10;
        n = n / 10;
        c++;
        if (c == (l - 2))
        {
            x = n;
        }
    }
    //checks the start of the credit cards and runs the correct output
    if (x == 34 || x == 37)
    {
        printf("AMEX\n");
    }
    else if (x == 51 || x == 52 || x == 53 || x == 54 || x == 55)
    {
        printf("MASTERCARD\n");
    }
    else if (x / 10 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
        return;
    }
}
int main()
{ 
    ccNumber = userInput();
    long int ccCopy = ccNumber;
    int ccLength = checkLength(ccNumber);
    //this is the logic that checks the length and states INVALID if not.
    if (ccLength != 13 && ccLength != 15 && ccLength != 16)
    {
        printf("INVALID\n");
        return 0;
    }
    int ccValidity = checkValidity(ccCopy, ccLength);
    if (ccValidity == 0)
    {
        ccCompany(ccCopy, ccLength);
    }
    else
    {
        printf("INVALID\n");
        return 0;
    }
    return 0;
}
