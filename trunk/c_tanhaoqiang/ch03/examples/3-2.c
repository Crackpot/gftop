/*
 * P 43
 * 整形变量的定义和使用
 * */
#include <stdio.h>
void main(){
    int a,b,c,d;
    unsigned u;
    a=12;b=-24;u=10;
    printf("a=%d,b=%d\n",a,b);
    c=a+u;
    d=b+u;
    printf("a+u=%d,b+u=%d\n",c,d);
}
