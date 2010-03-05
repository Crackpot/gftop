/*
 * =====================================================================================
 *
 *       Filename:  4-01.c
 *
 *    Description:  输出单个字符 P73
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时44分11秒
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
    char a, b, c;
    a = 'B', b = 'O', c = 'Y';// 单个字符用单引号括起来
    putchar(a);putchar(b);putchar(c);putchar('\n');
    return 0;
}
