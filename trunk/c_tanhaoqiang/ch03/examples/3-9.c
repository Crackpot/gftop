/*
 * =====================================================================================
 *
 *       Filename:  3-9.c
 *
 *    Description:  有符号数据传送给无符号变量 P61
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 04时53分36秒
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
    unsigned a;
    int b = -1;
    a = b;// 将b的数值传送给a
    printf("-1传送给无符号变量a的结果为： a = %u\n", a);
    return 0;
}
