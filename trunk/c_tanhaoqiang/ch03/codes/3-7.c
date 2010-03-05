/*
 * =====================================================================================
 *
 *       Filename:  3-7.c
 *
 *    Description:  大小写字母的转换 P51
 *
 *        Version:  1.0
 *        Created:  2009年09月25日 05时43分32秒
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
    char charset[] = {'a', 'b', 'c', 'd', 'e',};
    char charset2[5] = {};
    int i;
    for (i = 0; i < 5; i++) {
        printf("%c",charset[i]);
        charset2[i] = charset[i] - 32;
        printf("%c",charset2[i]);
    }
    return 0;
}
