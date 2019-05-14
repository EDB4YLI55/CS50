#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

//mention functions called in main to prevent compiling errors.
string userInput();
char rotateLower();
char rotateUpper();

void usage()
{
    //this prints the usage.
    printf("usage: caesar <key>\n");
    exit(1);
}

int main(int argc, string argv[])
{
    string s;
    //this section just prints the usage if there is not an argument give, or if more than 1 argument is given.
    if (argc != 2)
    {
        usage();
    }
    //not sure if this is allowed, but changed the key to a integar to work with later on - wouldn't work as string.
    int k = atoi(argv[1]);
    if( k <= 1000000 && k > 0)
    {
         s = userInput();
    }
    else
    {
        usage();
    }
    //this calls for the user input, this is the plaintext that it will encrypt.
    
    //create the variable which I will save each character as when they are rotated
    char c;
    printf("ciphertext: "); 
    //loops around the individual characters in the string given.
    for (int x = 0, n = strlen(s); x < n; x++)
    {
        //if the character is a lowercase character
        if (s[x] >= 'a' && s[x] <= 'z')
        {   
            //call the roate lower function
            c = rotateLower(s[x], k);
        }
        //if the character is an uppercase character
        else if (s[x] >= 'A' && s[x] <= 'Z')
        {
            //call the rotate upper function
            c = rotateUpper(s[x], k);
        }
        //if the character is anything else, this could be a space, number or full stop, don't do anything.
        else
            c = s[x];
        //print the character, no new line so it joins the chars
        printf("%c", c);
    }
    printf("\n");
}

string userInput()
{
    //takes user input and saves it as a variable and returns it.
    string s = get_string("plaintext: ");
    return s;
}

char rotateLower(s, k)
{
    //this takes the single char from the array and the key, and applies the rotation policy.
    char c = (((s - 'a') + k) %26 + 'a');
    //returns the rotated char.
    return c;
}
char rotateUpper(s, k)
{
    //this takes the single char from the array and the key, and applies the rotation policy.
    char c = (((s - 'A') + k) % 26 + 'A');
    //returns the rotated char.
    return c;
}
