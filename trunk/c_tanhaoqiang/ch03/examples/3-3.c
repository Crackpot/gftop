/*
 * =====================================================================================
 *
 *       Filename:  3-3.c
 *
 *    Description:  整形数据的溢出  P44
 *
 *        Version:  1.0
 *        Created:  2009年09月25日 05时22分28秒
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
    int a, b;
    a = 32767;
    b = a + 1;
    printf("a = %d\nb = a + 1 = %d",a, b);
    return 0;
}

