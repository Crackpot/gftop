/*
 * =====================================================================================
 *
 *       Filename:  3-10.c
 *
 *    Description:  写出下面程序的运行结果 P67
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时37分30秒
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
    int i, j, m, n;
    i = 8;
    j = 10;
    m = ++i;
    n = j++;
    printf("%d, %d, %d, %d\n", i, j, m, n);
    return 0;
}
