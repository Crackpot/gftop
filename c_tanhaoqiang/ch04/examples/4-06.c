/*
 * =====================================================================================
 *
 *       Filename:  4-06.c
 *
 *    Description:  输出实数时的有效位数 P79
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 06时04分07秒
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
    float x, y;
    x = 111111.111;
    y = 222222.222;
    printf("%f\n", x + y);
    return 0;
}
