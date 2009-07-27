/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestEnhanceAssign.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestEnhanceAssign{
    public static void main(String[] args){
        //定义一个byte类型的变量
        byte a = 5;
        //下面的语句出错，因为5默认是int类型，a+5就是int类型。
        //把int类型赋给byte类型的变量，所以出错
        //a = a + 5;   
        System.out.println(a);
        //定义一个byte类型的变量
        byte b = 5;
        //下面的语句将不会出现错误
        b += 5;
        System.out.println(b);
    }
}
