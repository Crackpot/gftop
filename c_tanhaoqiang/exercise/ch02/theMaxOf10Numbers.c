/*
 * =====================================================================================
 *
 *       Filename:  theMaxOf10Numbers.c
 *
 *    Description:  是个数，找出最大值
 *
 *        Version:  1.0
 *        Created:  2009年09月14日 20时31分25秒
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
    int a, b, c, d, e, f, g, h, i, j, max;
    printf("请输入十个数，用逗号隔开：\n");
    scanf("%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,", &a, &b, &c, &d, &e, &f, &g, &h, &i, &j);
    printf("您输入的十个数分别为： %d, %d, %d, %d, %d, %d, %d, %d, %d, %d\n",a, b, c, d, e, f, g, h, i, j);
    max = a;
    if (max < b)
        max = b;
    if (max < c)
        max = c;
    if (max < d)
        max = d;
    if (max < e)
        max = e;
    if (max < f)
        max = f;
    if (max < g)
        max = g;
    if (max < h)
        max = h;
    if (max < i)
        max = i;
    if (max < j)
        max = j;
    printf("十个数中的最大值为：%d\n",max);
    return 0;
}

