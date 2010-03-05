/*
 * =====================================================================================
 *
 *       Filename:  4-03.c
 *
 *    Description:  无符号数据的输出 P77
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时52分41秒
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
    unsigned int a = 65535;
    int b = -2;
    printf("a = %d, %o, %x, %u\n", a, a, a, a);
    printf("b = %d, %o, %x, %u\n", b, b, b, b);
    return 0;
}
