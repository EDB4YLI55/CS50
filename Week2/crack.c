#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <math.h>

void usage();
void crack();

//this creates a string of all the possible chars I can use, It's starts with a null byte, so that I can start of with a password like this "\0\0\0\0\0A" later on.
string DICT = "\0ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

int main(int argc, string argv[])
{
    char salt[3];
    char hash[20];
    int x = 0;
    //this checks if an argument has been given, if not it will print the usage and return an error code 1.
    if (argc != 2)
    {
        usage();
        return 1;
    }
    else
    {
        char * input = argv[1];
        for(int i=0; i < strlen(input); i++)
        {
            //this creates a variable called salt and stores the first two chars of the argument in it.
            salt[0] = input[0];
            salt[1] = input[1];
            break;
        }
        for(int i=0; i < strlen(input); i++)
        {
            if (i > 2)
            {
                //this is ugly but this does another loop and stores the remaining chars of the hash in a variable called hash
                x = (i - 3);
                hash[x] = input[i];
            }
        }
        //calls the cracking process
        crack(salt, hash);
    }
}
void usage()
{
    printf("Usage: crack <hash>\n");
}

void crack(string salt, string hash, string input)
{
    //creates a dummy password full of null bytes
    char pass[6] = "\0\0\0\0\0\0";
    for (int loop4 = 0; loop4 < 53; loop4++)
    {
        for (int loop3 = 0; loop3 < 53; loop3++)
        {
            for (int loop2 = 0; loop2 < 53; loop2++)
            {
                for (int loop1 = 0; loop1 < 53; loop1++)
                {
                    for (int loop0 = 0; loop0 < 53; loop0++)
                    {
                        //this section is weird too, the most inside loop, loops around fast, so I had to change the chars of the dummy pass like this.
                        pass[0] = DICT[loop0];  // 1)
                        pass[1] = DICT[loop1]; // 2)
                        pass[2] = DICT[loop2];  // 3)
                        pass[3] = DICT[loop3]; // 4)
                        pass[4] = DICT[loop4];  // 5)
                        //this tests the hash against the original argument, if it is a match it prints the password
                        if (strcmp(crypt(pass, salt), input) == 0)
                        {
                            printf("%s\n", pass);
                            return;
                        }
                    }
                }
            }
        }
    }
}