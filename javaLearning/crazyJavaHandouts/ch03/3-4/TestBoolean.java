/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestBoolean.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestBoolean
{
    public static void main(String[] args)
    {
        // 定义b1的值为true
        boolean b1 = true;
        System.out.println(b1);
        // 定义b2的值为false
        boolean b2 = false;
        System.out.println(b2);
        // 使用boolean和字符串进行连接运算，boolean会自动转换成字符串
        String str = true + "";
        System.out.println(str);
    }
}
