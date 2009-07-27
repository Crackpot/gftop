/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestMod.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestMod
{
    public static void main(String[] args)
    {
        double a = 5.2;
        System.out.println(a);
        double b = 3.1;
        System.out.println(b);
        double mod = a % b;
        //mod的值为2.1
        System.out.println(mod);
        //输出非数NaN
        System.out.println("5对0.0求余的结果是：" + 5 % 0.0);
        //输出非数NaN
        System.out.println("-5对0.0求余的结果是：" + -5 % 0.0);
        //输出0.0
        System.out.println("0对5.0求余的结果是：" + 0 % 5.0);
        //输出非数NaN
        System.out.println("0对0.0求余的结果是：" + 0 % 0.0);
        //下面的代码将会出现异常 java.lang.ArithmeticException: / by zero
        System.out.println("5对0求余的结果是：" + 5 % 0);
    }
}
