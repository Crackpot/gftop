/*
 * =====================================================================================
 *
 *       Filename:  3-7.c
 *
 *    Description:  编译密码 P67
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时07分18秒
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
    char string[] = "China";
    printf("%s\n", string);

    int i;
    for(i = 0; i <5; i++) {
        string[i] += 4;
    }
    printf("%s\n", string);
    return 0;
}
