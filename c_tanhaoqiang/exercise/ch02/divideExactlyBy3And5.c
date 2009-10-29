/*
 * =====================================================================================
 *
 *       Filename:  divideExactlyBy3And5.c
 *
 *    Description:  判断一个数n能否同时被3和5整除
 *
 *        Version:  1.0
 *        Created:  2009年09月14日 21时15分16秒
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
    int n;
    printf("请输入整数n来判断是否可以同时被3和5整除\n");
    scanf("%d",&n);
    if ((n % 3 == 0) && (n % 5 == 0)){
        printf("n = %d 能同时被3和5整除！\n",n);
    } else {
        printf("n = %d 不能同时被3和5整除！\n",n);
    }
    return 0;
}
