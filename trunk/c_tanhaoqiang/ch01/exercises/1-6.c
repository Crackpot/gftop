/*
 * =====================================================================================
 *
 *       Filename:  1-6.c
 *
 *    Description:  求三个数中的最大值          P13
 *
 *        Version:  1.0
 *        Created:  2009年09月18日 20时02分26秒
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
    int larger(int x, int y);
    int a, b, c, d;
    printf("请输入三个数字：\n");
    scanf("%d,%d,%d",&a, &b, &c);
    d = larger(larger(a, b), c);
    printf("三个数中的最大值为：%d\n",d);
    return 0;
}
int larger(int x, int y) {
    int z;
    if (x > y) {
        z = x;
    } else {
        z = y;
    }
    return z;
}


