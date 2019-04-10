    }
    else
    {
        return 1;
    }
}


int main()
{ 
    ccNumber = userInput();
    long int ccCopy = ccNumber;
    int ccLength = checkLength(ccNumber);
    if (ccLength != 13 && ccLength != 15 && ccLength != 16)
    {
        printf("INVALID\n");
        main();
    }
    int ccValidity = checkValidity(ccCopy, ccLength);
    if (ccValidity == 0)
    {
        return 0;//CODE HERE TO CHECK COMPANY
    }
    else
    {
        printf("INVALID\n");
        return 1;
    }
    return 0;
}
