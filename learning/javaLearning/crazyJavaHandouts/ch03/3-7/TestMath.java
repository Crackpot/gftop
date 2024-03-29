/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestMath.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestMath
{
    public static void main(String[] args)
    {
        //定义变量a为3.2
        double a = 3.2;
        System.out.println(a);
        //求a的5次方，并将计算结果赋为b 
        double b = Math.pow(a , 5);
        System.out.println(b);
        //求a的平方根，并将结果赋给c
        double c = Math.sqrt(a);
        System.out.println(c);
        //计算随机数，返回一个0~1之间的伪随机数
        double d = Math.random();
        System.out.println(d);
        System.out.println(d * 10);
        System.out.println((int)(d * 10));
        //求1.57的sin函数值:1.57被当成弧度数
        double e = Math.sin(1.57);
        System.out.println(e);
    }
}
