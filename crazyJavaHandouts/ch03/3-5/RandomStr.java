/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:AutoConversion.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class RandomStr
{
    public static void main(String[] args)
    {
        //定义一个空字符串
        String result = "";
        //进行20次循环
        for(int i = 0; i < 21; i ++)
        {
            //生成一个97到122之间的整数
            int intValue = (int)(Math.random() * 26 +97);
            //将intValue强制转换为char后连接到result后面
            result += (char)intValue;
        }
        //输出随机字符串
        System.out.println("系统产生的随机字符串为：\n" + result);
    }
}
