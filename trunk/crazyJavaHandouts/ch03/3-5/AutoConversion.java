/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:AutoConversion.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class AutoConversion
{
    public static void main(String[] args)
    {
        int a = 6;
        //int类型可以自动转换为float类型
        float f = a;
        //下面将输出6.0
        System.out.println(f);
        //定义一个byte类型的整数变量
        byte b = 9;
        System.out.println(b);
        //  下面代码将出错，byte型不能自动类型转换为char型
        //char c = b;
        //下面是byte型变量可以自动类型转换为double型
        double d = b;
        //下面将输出9.0
        System.out.println(d);
    }
}
