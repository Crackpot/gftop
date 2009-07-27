/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestBitOperator.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestBitOperator
{
    public static void main(String[] args)
    {
        //将输出1
        System.out.println(5 & 9);
        //将输出13
        System.out.println(5 | 9);
        //按位取反
        //正数按位取反是原数加1的相反数
        System.out.println(~ 0 + "\t" + ~ 1 +"\t" + ~ 2 +"\t" + ~ 3);
        //负数按位取反是原数加1的相反数
        System.out.println(~ 0 + "\t" + ~ -1 +"\t" + ~ -2 +"\t" + ~ -3);
        //将输出-6
        System.out.println(~ 5);
        //将输出4
        System.out.println(~ -5);
        //按位异或
        //将输出12
        System.out.println(5 ^ 9);
        //左移运算
        //输出20
        System.out.println(5 << 2);
        //输出-20
        System.out.println(-5 << 2);
        //右移运算
        //输出1
        System.out.println(5 >> 2);//有符号右移运算 左边空出来的位以原来的符号填充
        //输出-2
        System.out.println(-5 >> 2);
        //输出1
        System.out.println(5 >>> 2);
        //输出1073741822 
        System.out.println(-5 >>> 2);//无符号右移运算 左边空出来的位总是以0来填充
    }
}
