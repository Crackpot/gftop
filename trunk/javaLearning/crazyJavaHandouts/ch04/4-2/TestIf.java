/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestIf.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestIf
{
    public static void main(String[] args)
    {
        int age = 30;
        if (age > 20)
        //只有当age>20时，下面花括号括起来的语句块才会执行    
        //花括号括起来的语句是一个整体，要么一起被执行，要么一起不执行
        {
            System.out.println("年龄大于20");
            System.out.println("20岁以上的人应当学会承担责任");
        }

        int a = 5;
        if (a > 4)
            //如果a>4，执行下面的执行体，只有一行代码作为代码块
            System.out.println("a大于4");
        else
            //否则，执行下面的执行体，只有一行代码作为代码块
            System.out.println("a不大于4");

        int b = 5;
        if (b > 4)
            //如果b>4，执行下面的执行体，只有一行代码作为代码块
            System.out.println("b大于4");
        else
            //否则，执行下面的执行体
            b--;
            //对于下面的代码而言，它已经不是条件执行体的一部分，因此，它总是会被执行
            System.out.println("b不大于4");

        int c = 5;
        if (c > 4)
            //如果c>4，执行下面的执行体，将只有c--;一行代码为条件执行体
            c--;
            System.out.println("c的值为：" + c);
            //下面是一行普通代码，不属于条件执行体
            System.out.println("c大于4");
        //此处的else将没有if语句，因此编译出错
        //else
            //否则，执行下面的执行体，只有一行代码作为代码块
            System.out.println("c不大于4");
    }
}
