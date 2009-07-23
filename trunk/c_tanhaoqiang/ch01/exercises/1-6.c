/*
 * P 13
 * 求三个数中的最大值
 * */
#include <stdio.h>
void main(){
    int larger(int x,int y);
    int a,b,c,d,e;
    printf("请输入三个数字：\n");
    scanf("%d,%d,%d",&a,&b,&c);
    d=larger(larger(a,b),c);
    printf("三个数中的最大值为:%d\n",d);
}
int larger(int x,int y){
    int z;
    if (x>y) z=x;
    else z=y;
    return (z);
}
