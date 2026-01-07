#include<stdio.h>

int process[50];
    int n;
    int bt[50];

void calcWT_TAT(int wt[n],int tat[n],int bt[n])
{
    wt[0]=0;
    for(int i=1;i<n;i++)
    {
       wt[i]=wt[i-1]+bt[i-1];
    }
    for(int i=0;i<n;i++)
    {
        tat[i]=bt[i]+wt[i];
    }
}
void ps(int process[], int n, int bt[],int priority[])
{
    int wt[n];
    int tat[n];
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(priority[i]<priority[j])
            {
                int temp=priority[i];
                priority[i]=priority[j];
                priority[j]=temp;

                 temp=process[i];
                process[i]=process[j];
                process[j]=temp;

                temp=bt[i];
                bt[i]=bt[j];
                bt[j]=temp;
                
            }
        }
    }
   calcWT_TAT (wt,tat,bt);
   printf("-------------Priority Scheduling Algorithm------------\n");
    printf("waiting time:");
    for(int i=0;i<n;i++)
    {
        printf("%d ",wt[i]);
    }
    printf("\n");
    printf("Turn around time:");
    for(int i=0;i<n;i++)
    {
        printf("%d ",tat[i]);
    }
    printf("\n");
    int avgWT=0;
    int avgTAT=0;
    for(int i=0;i<n;i++)
    {
        avgWT=avgWT+wt[i];
        avgTAT=avgTAT+tat[i];
    }
    printf("--------------------------------\n");
    printf("Averge Waiting Time:%.2f\n",((float)avgWT/(float)n));
    printf("Averge Turn Around  Time:%.2f\n",((float)avgTAT/(float)n));
    
    printf("--------------------------------");


}

int main()
{
    
    printf("Enter the number of processes: "); 
    scanf("%d",&n);
    
    
    for(int i=0;i<n;i++)
    {
       
       printf("Enter the Process ID for process %d: ", i + 1); 
        scanf("%d", &process[i]);
    }

    
    printf("Enter the burst times:\n"); 
    for(int i=0;i<n;i++)
    {
        printf("Burst Time for P%d: ", process[i]);
        scanf("%d", &bt[i]);
    }
    
  
    printf("\n--- Entered Data ---\n");
    printf("Processes IDs: ");
    for(int i=0;i<n;i++)
    {
        printf("%d ",process[i]);
    }
    
    
    printf("\nBurst Times: ");
    for(int i=0;i<n;i++)
    {
        printf("%d ",bt[i]);
    }
    printf("\n");
   int priority[n];
   printf("enter the priority:");
   for(int i=0;i<n;i++)
    {
        printf("priority for P%d: ", process[i]);
        scanf("%d", &priority[i]);
    }
    ps( process,  n,  bt,priority);

}