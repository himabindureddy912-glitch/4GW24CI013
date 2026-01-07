// Non-Preemptive SJF (Shortest Job First) CPU Scheduling

#include <stdio.h>

int main() {
    int n;
    int at[10], bt[10], ct[10], tat[10], wt[10], completed[10] = {0};
    int time = 0, done = 0;
    float avg_tat = 0, avg_wt = 0;
    printf("SJF: ");
    printf("Enter number of processes: ");
    scanf("%d", &n);

    // Input Arrival Time and Burst Time
    for (int i = 0; i < n; i++) {
        printf("Enter Arrival Time and Burst Time for P%d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
    }

    // SJF Scheduling
    while (done < n) {
        int idx = -1;
        int min_bt = 9999;

        for (int i = 0; i < n; i++) {
            if (at[i] <= time && !completed[i] && bt[i] < min_bt) {
                min_bt = bt[i];
                idx = i;
            }
        }

        if (idx == -1) {
            time++;  // CPU idle
        } else {
            time += bt[idx];
            ct[idx] = time;
            completed[idx] = 1;
            done++;
        }
    }

    // Calculate TAT and WT
    for (int i = 0; i < n; i++) {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];
        avg_tat += tat[i];
        avg_wt += wt[i];
    }

    avg_tat /= n;
    avg_wt /= n;

    // Output
    printf("\nProcess\tAT\tBT\tCT\tTAT\tWT\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
               i + 1, at[i], bt[i], ct[i], tat[i], wt[i]);
    }

    printf("\nAverage Turnaround Time = %.2f", avg_tat);
    printf("\nAverage Waiting Time = %.2f\n", avg_wt);

    return 0;
}
