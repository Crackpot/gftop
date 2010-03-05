/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestThree.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestThree{
    public static void main(String[] args){
    	// 三目运算
        String str = 5 > 3 ? "5大于3" : "5不大于3";
        System.out.println(str);
        //将上面的写法转换成if else写法：
        String str2 = null;
        if (5 > 3) {
            str2 = "5大于3";
        }
        else {
            str2 = "5不大于3";
        }
        System.out.println(str2);
    }
}
