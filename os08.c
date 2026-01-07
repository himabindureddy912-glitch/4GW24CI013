// Best Fit Memory Allocation – Simple C Program

#include <stdio.h>

int main() {
    int m, n;

    printf("Enter number of memory blocks: ");
    scanf("%d", &m);

    int block[m];
    for (int i = 0; i < m; i++) {
        printf("Enter size of block %d: ", i + 1);
        scanf("%d", &block[i]);
    }

    printf("Enter number of processes: ");
    scanf("%d", &n);

    int process[n], allocation[n];

    for (int i = 0; i < n; i++) {
        printf("Enter size of process %d: ", i + 1);
        scanf("%d", &process[i]);
        allocation[i] = -1;   // not allocated
    }

    // Best Fit Allocation
    for (int i = 0; i < n; i++) {
        int best = -1;
        for (int j = 0; j < m; j++) {
            if (block[j] >= process[i]) {
                if (best == -1 || block[j] < block[best])
                    best = j;
            }
        }

        if (best != -1) {
            allocation[i] = best;
            block[best] -= process[i];
        }
    }

    // Output
    printf("\nProcess\tSize\tBlock\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t", i + 1, process[i]);
        if (allocation[i] != -1)
            printf("%d\n", allocation[i] + 1);
        else
            printf("Not Allocated\n");
    }

    return 0;
}
