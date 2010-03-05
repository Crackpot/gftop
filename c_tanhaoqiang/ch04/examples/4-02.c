/*
 * =====================================================================================
 *
 *       Filename:  4-02.c
 *
 *    Description:  输入单个字符 P74
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时49分29秒
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
    char c;
    c = getchar(); // 如若输入的是字符串，它只取其第一个字符。
    putchar(c);
    putchar('\n');
    return 0;
}
