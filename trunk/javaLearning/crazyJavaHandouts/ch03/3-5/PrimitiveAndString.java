/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:PrimitiveAndString
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class PrimitiveAndString
{
    public static void main(String[] args)
    {
        //下面代码是错的，因为5是一个整数，不能直接赋值给一个字符串
        //String str1 = 5;
        //一个基本类型值和字符串进行连接运算时，基本类型值自动转换为字符串
        String str2 = 3.5f + "";
        //下面输出3.5
        System.out.println(str2);
        //下面语句输出7Hello!
        System.out.println(3 + 4 + "Hello!");
        //下面这句将输出Hello34，因为Hello+3将把3当成字符串处理
        System.out.println("Hello!" + 3 + 4);
    }
}

