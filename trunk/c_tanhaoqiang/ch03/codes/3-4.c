/*
 * =====================================================================================
 *
 *       Filename:  3-4.c
 *
 *    Description:  浮点数据的舍入误差  P47
 *
 *        Version:  1.0
 *        Created:  2009年09月25日 05时25分22秒
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
    float a, b;
    a = 123456.789e5;
    b = a + 20;
    printf("a = 123456.789e5\nb = a + 20 = %f\n",b);
    return 0;
}

