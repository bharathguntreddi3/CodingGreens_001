#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    long long candy;
    int t;
    int i;
    long long j;
    int count = 0;
    scanf("%d\n", &t);
    for(i=0; i<t; i++){
        scanf("%lld", &candy);     // looping over the total candies
        for(j=1; j<=candy; j++){
            candy = candy - (j*j);    // giving the candies to the jth children with j2 candies 
            if(candy < 0){
                break;
            }
            else{
                count++;
            }
        }
        printf("%d\n", count);
        count = 0;
    }
    return 0;
}