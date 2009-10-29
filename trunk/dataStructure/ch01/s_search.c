/*
 * =====================================================================================
 *
 *       Filename:  s_search.c
 *
 *    Description:  设计一个顺序查找的程序，运用顺序查找法来查找数据中的某一个特定值
 *
 *        Version:  1.0
 *        Created:  2009年09月21日 03时52分52秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Crackpot 
 *        Company:  
 *
 * =====================================================================================
 */

#include <stdio.h>

int Data[20] = { /* 输入数据数组 */
    1, 7, 9, 12, 15,
    16, 20, 32, 35, 67,
    78, 80, 83, 89, 90,
    92, 97, 108, 120, 177
};
int Counter = 1; /* 查找计数变量 */

/*--------------------------------------*/
/* 顺序查找                             */
/*--------------------------------------*/
int Seq_Search (int Key) {
    int i; /* 数据索引计数变量 */

    for (i = 0; i < 20; i++) {
        //printf("[%d]",Data[i]); /* 输出数据 */
        if (Key == Data[i]) /* 查找到数据时 */
            return 1;
        Counter++; /* 计数器递增 */
    }
    return 0;
}


/*--------------------------------------*/
/* 主程序                               */
/*--------------------------------------*/
int main() {
    int KeyValue; /* 欲查找数据变量 */

    int i;
    printf("The data array is :\n");
    for (i = 0; i < 20; i++) { /* 输出数据 */
        printf("Data[%d] = %d\t",i, Data[i]);
        if ((i + 1) % 5 == 0) printf("\n"); /* 一行输出5个数据，换行 */
    }

    printf("Please enter your key value : ");
    scanf("%d",&KeyValue); /* 输入欲查找值 */

    if (Seq_Search(KeyValue)) /* 调用顺序查找子程序 */
        printf("\nSearch time = %d\n",Counter); /* 输出查找次数 */
    else
        printf("No found!!\n"); /* 输出没有找到数据 */
    return 0;
}
