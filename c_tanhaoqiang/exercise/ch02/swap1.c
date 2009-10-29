/*
 * =====================================================================================
 *
 *       Filename:  swap1.c
 *
 *    Description:  两个变量，交换两个值
 *
 *        Version:  1.0
 *        Created:  2009年09月14日 20时06分47秒
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
    int a, b, c;
    printf("请输入两个变量的值a, b：\n");
    scanf("%d,%d",&a, &b);
    printf("两个变量值交换之前的情况是：a = %d ,b = %d\n",a, b);
    c = a;// c临时存放a的值，a就可以去做其他事情了
    a = b;// a存放b的值，b没用了
    b = c;// 原来a的值就给c了
    printf("两个变量值交换之后的结果为：a = %d ,b = %d\n",a, b);
    return 0;
}
