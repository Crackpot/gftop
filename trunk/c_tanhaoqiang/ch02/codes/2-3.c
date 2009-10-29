/*
 * =====================================================================================
 *
 *       Filename:  2-3.c
 *
 *    Description:  判断2000年到2500年中的每一年是否是闰年，并将结果输出             P17
 *
 *        Version:  1.0
 *        Created:  2009年09月18日 20时59分11秒
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
    int year;
    int isLeapYear(int year);
    for (year = 2000; year <= 2500; year++) {
        if (isLeapYear(year)) {
            printf("%d年是闰年\n",year);
        } else {
            printf("%d年不是闰年\n",year);
        }
    }
    return 0;
}
int isLeapYear(int year) {
    int flag = 0;
    if ((year % 4 ==0 && year % 100 != 0) || (year % 100 == 0 && year %400 == 0)) flag = 1;
    return flag;
}
