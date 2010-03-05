/*
 * =====================================================================================
 *
 *       Filename:  3-9.c
 *
 *    Description:  x + a % 3 * (int)(x + y) % 2 / 4 设 x = 2.5, a = 7, y = 4.7
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 05时24分15秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */

#include<stdio.h>
int main() {
    float x = 2.5, y = 4.7, z;
    int a = 7;
    z = x + a % 3 * (int)(x + y) % 2 / 4; 
    printf("%f\n", z);
    return 0;
}
