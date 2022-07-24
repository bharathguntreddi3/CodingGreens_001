#include<assert.h>
#include<ctype.h>
#include<limits.h>
#include<math.h>
#include<stdbool.h>
#include<stddef.h>
#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int a[6][6];
    int i,j;
    for(i = 0;i<6;i++){
        for(j=0;j<6;j++){
            scanf("%d",&a[i][j]);  // reading the values from the user
        }
    }
    int n=-100 ,s =0;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            s = 0;
            // taking the indices values for the hourglass containing all the indices for the all the hourglasses in the 6*6 matrix
            s+=a[i][j];
            s+=a[i][j+1];
            s+=a[i][j+2];
            s+=a[i+1][j+1];
            s+=a[i+2][j];
            s+=a[i+2][j+1];
            s+=a[i+2][j+2];
            if(s > n){
                n = s;
            }
        }
    }
    printf("%d", n);
    return 0;
    
}