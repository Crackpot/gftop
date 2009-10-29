/*
 * =====================================================================================
 *
 *       Filename:  theMaxOf3Numbers.c
 *
 *    Description:  输入三个数字，求出最大值
 *
 *        Version:  1.0
 *        Created:  2009年09月14日 19时56分32秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Crackpot 
 *        Company:  
 *
 * =====================================================================================
 */
#include <stdio.h>

int main() {
    int a, b, c, max;
    printf("请输入三个数a, b, c：\n");
    scanf("%d, %d ,%d",&a, &b, &c);
    max = a;
    if (max < b)
        max = b;
    if (max < c)
        max = c;
    printf("三个数中最大值为：%d\n", max);
    return 0;
}
