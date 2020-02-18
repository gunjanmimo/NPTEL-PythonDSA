#include<stdio.h>
#include<stdlib.h>
int max(int a, int b){
    return (a>b)?a:b;
}
int knapsack(int W, int wt[], int val[], int n) 
{ 
   if (n == 0 || W == 0) 
       return 0; 
  
   if (wt[n-1] > W) 
       return knapsack(W, wt, val, n-1); 
   
   else return max( val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), 
                    knapsack(W, wt, val, n-1) 
                  ); 
} 
int main(){
    int n;
    printf("Enter the no of element: \n");
    scanf("%d",&n);
    int weight[n];
    int val[n];
    int capacity;
    printf("Enter the capacity of the bag:\n");
    scanf("%d",&capacity);
    printf("Enter the weight of each elements:\n");
    for(int i=0;i<n;i++){
        scanf("%d",&weight[i]);
    }
    printf("Enter the value of each elements:\n");
    for(int i=0;i<n;i++){
        scanf("%d",&val[i]);
    }
    knapsack(capacity, weight, val, n);


    
}

