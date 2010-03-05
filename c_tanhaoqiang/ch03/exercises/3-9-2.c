/*
 * =====================================================================================
 *
 *       Filename:  3-9-2.c
 *
 *    Description:  (float)(a + b) / 2 + (int)x % (int)y 设a = 2, b = 3.5, y = 2.5
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时31分58秒
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
    int a = 2, b = 3;
    float x = 3.5, y = 2.5, z;
    z = (float)(a + b) / 2 + (int)x % (int)y;
    printf("%f\n", z);
    return 0;
}
