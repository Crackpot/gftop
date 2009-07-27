/**
 * Description:
 * <br/>Copyright (C), 2005-2008, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:AutoPromote.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class AutoPromote
{
    public static void main(String[] args)
    {
        //定义一个short类型变量
        short sValue = 5;
        System.out.println(sValue);
        //表达式中的sValue将自动提升到int类型，则右边的表达式类型为int
        //将一个int类型赋给short类型的变量将发生错误
        //sValue = sValue - 2;
        byte b = 40;
        char c = 'a';
        int i = 23;
        double d = .314;
        //右边表达式中在最高等级操作数为d(double型)
        //则右边表达式的类型为double型，故赋给一个double型变量
        double result = b + c + i * d;
        //将输出144.222
        System.out.println(result);
        int val = 3;
        //右边表达式中2个操作数都是int，故右边表达式的类型为int
        //因此，虽然23/3不能除尽，依然得到一个int整数
        int intResult = 23 / val;
        //将输出7
        System.out.println(intResult);
        //输出字符串Hello!a7
        System.out.println("Hello!" + 'a' + 7);
        //输出字符串104Hello!
        System.out.println('a' + 7 + "Hello!");
    }
}
