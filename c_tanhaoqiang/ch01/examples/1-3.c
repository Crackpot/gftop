/*
 * P 5
 * 求两个数中较大者
 * */
#include <stdio.h>
void main(){
    int max(int x,int y);
    int a,b,c;
    printf("Input two numbers:\n");
    scanf("%d,%d",&a,&b);
    c=max(a,b);
    printf("max=%d\n",c);
}
int max(int x,int y){
    int z;
    if (x>y) z=x;
    else z=y;
    return(z);
}
