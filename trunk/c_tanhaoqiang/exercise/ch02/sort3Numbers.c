/*
 * =====================================================================================
 *
 *       Filename:  sort3Numbers.c
 *
 *    Description:  三个数字，从小到大排序
 *
 *        Version:  1.0
 *        Created:  2009年09月14日 20时48分02秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Crackpot 
 *        Company:  
 *
 * =====================================================================================
 */

#include<stdio.h>

int main() {
    int a, b, c, swap;
    printf("请输入三个数a, b, c\n");
    scanf("%d,%d,%d",&a,&b,&c);
    printf("您输入的三个数分别为：  %d, %d, %d\n",a, b, c);
    if (a > b) {// 若a > b，互换
        swap = b;
        b = a;
        a = swap;
    }
    if (a > c) {// 若a > c，互换
        swap = c;
        c = a;
        a = swap;
    }
    if (b > c) {// 若b > c，互换
        swap = b;
        b = c;
        c = swap;
    }
    printf("排序后的结果为：%d, %d, %d\n",a, b, c);
    return 0;
}
