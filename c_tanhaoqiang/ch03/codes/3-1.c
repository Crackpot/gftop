/*
 * =====================================================================================
 *
 *       Filename:  3-1.c
 *
 *    Description:  符号常量的使用          P38
 *
 *        Version:  1.0
 *        Created:  2009年09月25日 05时15分05秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Crackpot
 *        Company:  
 *
 * =====================================================================================
 */

#define PRICE 30
#include <stdio.h>

int main() {
    int num,total;
    num = 10;
    total = num * PRICE;
    printf("total = %d\n",total);
    return 0;
}
