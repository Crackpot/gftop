/*
 * =====================================================================================
 *
 *       Filename:  3-8.c
 *
 *    Description:  强制类型转换 P57
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 04时42分38秒
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
    float x;
    int i;
    x = 3.6;
    i = (int)x;// 强制转换
    printf("x=%f, i=%d\n", x, i);
    return 0;
}
