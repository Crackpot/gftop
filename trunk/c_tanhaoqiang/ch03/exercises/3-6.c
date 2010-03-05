/*
 * =====================================================================================
 *
 *       Filename:  3-6.c
 *
 *    Description:  写出以下程序的运行结果 P66
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时01分36秒
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
    char c1 = 'a', c2 = 'b', c3 = 'c', c4 = '\101', c5 = '\106';
    printf("a%cb%c\tc%c\tabc\n", c1, c2, c3);
    printf("\t\b%c %c\n", c4, c5);
    return 0;
}
