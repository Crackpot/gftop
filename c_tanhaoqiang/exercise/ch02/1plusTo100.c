/*
 * =====================================================================================
 *
 *       Filename:  1plusTo100.c
 *
 *    Description:  从1加到100
 *
 *        Version:  1.0
 *        Created:  2009年09月14日 21时11分12秒
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
    int i, sum = 0;
    for (i = 0; i <= 100; i ++) {
        sum += i;
    }
    printf("1 + 2 + 3 + …… + 100 = %d\n",sum);
    return 0;
}
