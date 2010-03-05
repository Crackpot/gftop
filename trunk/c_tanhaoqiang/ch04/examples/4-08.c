/*
 * =====================================================================================
 *
 *       Filename:  4-08.c
 *
 *    Description:  输出实数时指定小数位数 P79
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 06时11分00秒
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
    float f = 123.456;
    printf("%f  %10f  %10.2f  %.2f  %-10.2f\n", f, f, f, f, f);
    return 0;
}
