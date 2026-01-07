#include<stdio.h>
#include<unistd.h>
int main(){
    pid_t pid;
    pid_t fork();
    if(pid==-1)
    {
       perror("fork");
       return 1;
    }
    else if(pid==0){
        printf("child process\n");
        excel("bin/ls","ls","-l",NULL);
    }
    else {
        printf("parent process\n");
        wait(NULL);
        printf("child process finished\n");
    }
  return 0;
}