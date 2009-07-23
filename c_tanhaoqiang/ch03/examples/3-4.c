/*
 * P 47
 * 浮点数据的舍入误差
 * */
#include<stdio.h>
void main(){
    float a,b;
    a=123456.789e5;
    b=a+20;
    printf("a=123456.789e5\nb=a+20=%d\n",b);
}
