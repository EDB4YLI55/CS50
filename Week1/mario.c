#include <stdio.h>
#include <cs50.h>

void hash();
void space();

int main(void) 
{ 
   //set variables
   int h;
   int s;
   int x;
   //get user input
   h = height();
   //checks user input is within valid range, if not re-prompts
   while (h < 1 || h > 8) 
   {    
       h = height();
   }
   //set spaces value
   s = h - 1;
   //for loop to increase printed hashes to max of height
   for (x = 1; x <= h; x++) 
   { 
       //calls the space function with the amount of spaces  
       space(s);   
       //calls the hash function with the amount of hashes
       hash(x);    
       printf("  ");
       hash(x);
       //reduces the space count
       s--;        
       printf("\n");
   }
}

void hash(int h) 
{
    for (int x = 0; x < h; x++) 
    {
        printf("#");
    }
}
void space(int s) 
{
    for (int x = 0; x < s; x++) 
    {
        printf(" ");
    }
}
int height(void)
{
    int h = get_int("Height: ");
    return h;
}
