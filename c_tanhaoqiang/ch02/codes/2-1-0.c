/*
 * =====================================================================================
 *
 *       Filename:  2-1-0.c
 *
 *    Description:  求1到5的乘机                P15
 *
 *        Version:  1.0
 *        Created:  2009年09月18日 20时12分10秒
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
    int jiecheng1(int a);
    int jiecheng2(int a);
    printf("for循环计算出的5的阶乘为：%d\n",jiecheng1(5));
    printf("while循环计算出的5的阶乘为：%d\n",jiecheng2(5));
    return 0;
}

int jiecheng1(int a) {
    int result = 1;
    int i;
    for (i = 1; i <= 5; i++) {
        result *= i;
    }
    return result;
}

int jiecheng2(int a) {
    int result = 1;
    int i = 1;
    while (i <= a) {
        result *= i;
        i ++;
    }
    return result;
}
