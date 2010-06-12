/*
 * =====================================================================================
 *
 *       Filename:  4-10.c
 *
 *    Description:  输入三角形的三边长，求三角形面积 P86
 *
 *        Version:  1.0
 *        Created:  2010年03月01日 06时45分33秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Crackpot
 *        Company:  
 *
 * =====================================================================================
 */

#include<stdio.h>
#include<math.h>

int main() {
    float a, b, c, s, area;
    scanf("%f, %f, %f", &a, &b, &c);
    s = 1.0/2 * (a + b + c); // 三边和的一半
    area = sqrt(s * (s - a) * (s - b) * (s - c));
    printf("a = %7.2f,  b = %7.2f  ,c = %7.2f,  s = %7.2f\n", a, b, c, s);
    printf("area = %f",area);
    return 0;
}
