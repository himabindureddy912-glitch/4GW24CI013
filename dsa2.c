#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Read a string safely */
void readString(char str[], size_t maxlen, const char *label)
{
    int c;
    printf("Enter %s: ", label);

    if (fgets(str, (int)maxlen, stdin) == NULL)
    {
        str[0] = '\0';
        return;
    }

    size_t len = strlen(str);
    if (len > 0 && str[len - 1] == '\n')
    {
        str[len - 1] = '\0';
    }
    else
    {
        while ((c = getchar()) != '\n' && c != EOF);
    }
}

/* Find string length without strlen */
int stringLength(char str[])
{
    int len = 0;
    while (str[len] != '\0')
        len++;
    return len;
}
