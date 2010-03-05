/*
 * =====================================================================================
 *
 *       Filename:  4-09.c
 *
 *    Description:  用scanf函数输入数据 P82
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 06时27分40秒
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
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    printf("%d,%d,%d", a, b, c);
    return 0;
}
