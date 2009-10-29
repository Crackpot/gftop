/*
 * =====================================================================================
 *
 *       Filename:  1-3.c
 *
 *    Description:  求两个数中较大者            P5
 *
 *        Version:  1.0
 *        Created:  2009年09月18日 19时51分23秒
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
    int max (int x, int y);
    int a, b, c;
    printf("Input two numbers:\n");
    scanf("%d,%d",&a, &b);
    c = max(a, b);
    printf("max = %d\n",c);
    return 0;
}
int max(int x, int y) {
    int z;
    if (x > y) z = x;
    else z = y;
    return z;
}
