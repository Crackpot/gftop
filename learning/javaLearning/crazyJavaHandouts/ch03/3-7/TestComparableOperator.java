/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestComparableOperator.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestComparableOperator
{
    public static void main(String[] args)
    {
        System.out.println("5是否大于4.0：" + (5 > 4.0));//输出true
        System.out.println("5和5.0是否相等：" + (5 == 5.0));//输出true
        System.out.println("97和'a'是否相等：" + (97 == 'a'));//输出true
        System.out.println("true和false是否相等：" + (true == false));//输出false
        //创建两个TestComparableOperator对象，分别赋给t1和t2两个引用
        TestComparableOperator t1 = new TestComparableOperator();
        TestComparableOperator t2 = new TestComparableOperator();
        //t1和t2是同一个类的两个实例的引用，所以可以进行比较
        //但t1和t2引用不同的对象，所以返回false
        System.out.println("t1和t2是否相等：" + (t1 == t2));//输出false
        //直接将t1的值赋给t3，即让t3指向t1指向的对象
        TestComparableOperator t3 = t1;
        System.out.println("t1和t3是否相等：" + (t1 == t3));//输出true
        Integer a = new Integer(6);
        System.out.println("6的包装实例是否大于5.0：" + (a > 5.0));//输出true
        System.out.println("比较两个包装实例是否相等：" + (new Integer(2) == new Integer(2)));//输出flase
        //通过自动装箱，允许把基本类型值赋值给包装类的实例
        Integer ina = 2;
        Integer inb = 2;
        System.out.println("比较两个2自动装箱后是否相等：" + (ina == inb));//输出true
        Integer biga = 128;
        Integer bigb = 128;
        System.out.println("比较两个128自动装箱后是否相等：" + (ina == inb));//输出true
        //通过new调用构造起创建的两个String实例
        String aStr = new String("Helo");
        String bStr = new String("Helo");
        System.out.println("通过两个内容相同的字符串new出来的String实例是否相等：" + (aStr == bStr));//输出false
        //通过直接量赋值创建的两个String实例
        String cStr = "Hello";
        String dStr = "Hello";
        System.out.println("直接把两个内容相同的字符串赋给String变量是否相等："  + (cStr == dStr));//输出true
    }
} 
