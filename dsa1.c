#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAME_SIZE 20
#define DESCRIPTION_SIZE 100

typedef struct {
    char *name;          // Day name
    int date;            // Date
    char *description;   // Activity description
} Day;

/* Function to allocate memory */
void create(Day *week, int size) {
    for (int i = 0; i < size; i++) {
        week[i].name = (char *)malloc(NAME_SIZE * sizeof(char));
        week[i].description = (char *)malloc(DESCRIPTION_SIZE * sizeof(char));

        if (week[i].name == NULL || week[i].description == NULL) {
            fprintf(stderr, "Memory allocation failed\n");
            exit(EXIT_FAILURE);
        }
    }
}

/* Function to read data */
void read(Day *week, int size) {
    for (int i = 0; i < size; i++) {
        printf("\nEnter details for Day %d\n", i + 1);

        printf("Day Name: ");
        scanf("%s", week[i].name);

        printf("Date: ");
        scanf("%d", &week[i].date);

        printf("Activity Description: ");
        scanf(" %[^\n]", week[i].description);
    }
}

/* Function to display data */
void display(Day *week, int size) {
    printf("\n--- Week's Activity Details ---\n");
    for (int i = 0; i < size; i++) {
        printf("Day: %s | Date: %d | Activity: %s\n",
               week[i].name,
               week[i].date,
               week[i].description);
    }
}

int main() {
    int size = 7;

    Day *week = (Day *)malloc(size * sizeof(Day));
    if (week == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return EXIT_FAILURE;
    }

    create(week, size);
    read(week, size);
    display(week, size);

    /* Free allocated memory */
    for (int i = 0; i < size; i++) {
        free(week[i].name);
        free(week[i].description);
    }
    free(week);

    return 0;
}
