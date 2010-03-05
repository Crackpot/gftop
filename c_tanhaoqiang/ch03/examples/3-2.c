/*
 * =====================================================================================
 *
 *       Filename:  3-2.c
 *
 *    Description:  整形变量的定义和使用 P43
 *
 *        Version:  1.0
 *        Created:  2009年09月25日 05时18分04秒
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
    int a, b, c, d;
    unsigned u;
    a = 12; b = -24; u = 10;
    printf("a = %d, b = %d\n",a, b);
    c = a + u;
    d = b + u;
    printf("a + u = %d, b + u = %d\n",c, d);
    return 0;
}

