#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void usage();
char * userInput();
char rotateLower();
char rotateUpper();

int main(int argc, string argv[])
{
    string s;
    string k = argv[1];
    //this section just prints the usage if there is not an argument give, or if more than 1 argument is given.
    if (argc != 2)
    {
        usage();
    }
    else
    {
        for (int i = 0, n = strlen(argv[1]); i < n ; i++)
        {
            if (!isalpha(argv[1][i]))
            {
                usage();
            }
        } 
    }
    s = userInput();
    char c;
    int key;
    printf("ciphertext: ");
    for (int x = 0, n = strlen(s); x < n ; x++)
    {

        key = tolower(k[x % strlen(k)] - 'a');

        //printf("%i", key);
        //if the character is a lowercase character
        if (s[x] >= 'a' && s[x] <= 'z')
        {   
            //call the roate lower function
            c = rotateLower(s[x], key);
        }
        //if the character is an uppercase character
        else if (s[x] >= 'A' && s[x] <= 'Z')
        {
            //call the rotate upper function
            c = rotateUpper(s[x], key);
        }
        //if the character is anything else, this could be a space, number or full stop, don't do anything.
        else
            c = s[x];
        //print the character, no new line so it joins the chars
        printf("%c", c);
    }
    printf("\n");
}

void usage()
{
    //this prints the usage.
    printf("usage: vigenere <key>\n");
    exit(1);
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
    char c = (((s - 'A') + k) %26 + 'A');
    //returns the rotated char.
    return c;
}
