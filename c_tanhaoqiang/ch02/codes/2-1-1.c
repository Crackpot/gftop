/*
 * =====================================================================================
 *
 *       Filename:  2-1-1.c
 *
 *    Description:  求1到11之间奇数的乘机
 *
 *        Version:  1.0
 *        Created:  2009年09月18日 20时21分18秒
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
    int chengji1(int a);
    int chengji2(int a);
    printf("for循环求得1到11之间奇数的乘机为：%d\n",chengji1(11));
    printf("while循环求得1到11之间奇数的乘机为：%d\n",chengji2(11));
    return 0;
}

int chengji1(int a) {
    int result = 1;
    int i;
    for (i = 1; i <= a; i += 2) {
        //printf("%d",i);
        result *= i;
    }
    return result;
}

int chengji2(int a) {
    int result = 1;
    int i = 1;
    while (i <= a) {
        //printf("%d",i);
        result *= i;
        i +=2;
    }
    return result;
}
