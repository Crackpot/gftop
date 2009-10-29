/*
 * =====================================================================================
 *
 *       Filename:  fibn.c
 *
 *    Description:  设计一个求费氏级数的程序
 *
 *        Version:  1.0
 *        Created:  2009年09月21日 04时26分53秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Crackpot 
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>

/*----------------------------------------*/
/* 主程序                                 */
/*----------------------------------------*/
int main() {
    int Number;         /* 运算数值变量 */
    int FibN;           /* 费氏级数变量Fn */
    int FibN1;          /* 费氏级数变量Fn1 */
    int FibN2;          /* 费氏级数变量Fn2 */
    int i;              /* 循环计数变量 */

    printf("The Fibonacci Numbers \n");
    printf("Please enter a number(not ladger than 46): "); /* 输入数值 */
    scanf("%d",&Number);

    if (Number <= 1) {
        printf("The 1 number in array is 1\n");
        //printf("Fibonacci Numbers of %d = 1\n",Number);
        printf("Fibonacci[1] = 1\n");
    }
    else {
        /* 1 1 2 3 5 8 11 19 */
        FibN2 = 0;
        FibN1 = 1;
        printf("Fibonacci[1] = 1\n");
        //printf("The 1 number in array is 1\n");
        for (i = 2; i <= Number; i++) {
            FibN = FibN1 + FibN2;
            printf("Fibonacci[%d] = %d\n",i, FibN);
            //printf("The %d number in array is %d\n",Counter, FibN);
            FibN2 = FibN1;
            FibN1 = FibN;
        }
        //printf("Fibonacci Numbers of %d = %d\n",Number, FibN);
    }
    return 0;
}
