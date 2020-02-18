#include<stdio.h> 
int max(int a, int b) { return (a > b)? a : b; } 
int knapSack(int W, int wt[], int val[], int n) 
{ 
   if (n == 0 || W == 0) 
       return 0; 
  
   if (wt[n-1] > W) 
       return knapSack(W, wt, val, n-1); 
   
   else return max( val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                    knapSack(W, wt, val, n-1) 
                  ); 
} 
  
int main() 
{ 
    int n;
    printf("Enter the no of element: ");
    scanf("%d",&n);
    int wt[n],W;
    printf("Enter the capacity of the bag:");
    scanf("%d",&W);
    int val[n];
    printf("Enter value and weight of each element: \n");
    for (int i=0;i<n;i++){
        printf("Enter weight of element: \n");
        scanf("%d",&wt[i]);
        printf("Enter value of element: \n");
        scanf("%d",&val[i]);

    }
    printf("Answer: %d", knapSack(W, wt, val, n)); 
    return 0; 
} 