/*
 * =====================================================================================
 *
 *       Filename:  swap2.c
 *
 *    Description:  同样是两个变量交换的问题，但是不借助第三变量
 *
 *        Version:  1.0
 *        Created:  2009年09月14日 20时15分01秒
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
    printf("请输入两个变量的值a, b：\n");
    scanf("%d,%d",&a, &b);
    printf("两个变量值交换之前的情况是：a = %d ,b = %d\n",a, b);
    b = (a + b) - b;
}
