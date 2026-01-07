// Round Robin CPU Scheduling (Easy Version)

#include <stdio.h>

int main() {
    int n, tq;
    int bt[10], rem_bt[10], at[10];
    int wt[10] = {0}, tat[10] = {0};
    int time = 0, completed = 0;
    printf("RR:  \n ");
    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter Time Quantum: ");
    scanf("%d", &tq);

    // Input Arrival Time and Burst Time
    for (int i = 0; i < n; i++) {
        printf("Enter Arrival Time and Burst Time for P%d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        rem_bt[i] = bt[i];   // remaining burst time
    }

    // Round Robin Scheduling
    while (completed < n) {
        int executed = 0;
        for (int i = 0; i < n; i++) {
            if (at[i] <= time && rem_bt[i] > 0) {
                if (rem_bt[i] > tq) {
                    time += tq;
                    rem_bt[i] -= tq;
                } else {
                    time += rem_bt[i];
                    wt[i] = time - at[i] - bt[i];
                    tat[i] = time - at[i];
                    rem_bt[i] = 0;
                    completed++;
                }
            }
        }
    }

    // Output
    printf("\nProcess\tAT\tBT\tTAT\tWT\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\n",
               i + 1, at[i], bt[i], tat[i], wt[i]);
    }

    return 0;
}
