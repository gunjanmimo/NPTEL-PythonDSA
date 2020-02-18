#include<stdio.h>
#include<stdlib.h>
int Search(int array[], int n, int search){
    int mid, first,last;
    first=0;
    last=n-1;
    mid=(first+last)/2;
    while(first<last){
        if(array[mid]<search){
            first=mid+1;
        }
        else if(array[mid]==search){
            printf("\n\nItem found!\n\n");
        }
        else
        {
            last=mid-1;
        }
        mid=(first+last)/2;
    }
    if(first>last){
        printf("Item not found\n\n");
    }

}
void printarr(int arr[],int n){
    printf("\n\nElements>> \n");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}

int main(){
    int t=rand()%100,n;
    printf("Total test case >> %d",t);
    for(int i=0;i<t;i++){
        n=rand()%1000;
        printf("\n\nNumber of Elements >> %d\n\n",n);
        int array[n];
        for(int j=0;j<n;j++){
            array[j]=rand()%1000;
        }
        
        int search=rand()%1000;
        printf("Search item >> %d", search);
        //printarr(array, n);
        Search(array, search,n);
    }

}