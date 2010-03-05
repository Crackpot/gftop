/**
 * Description:
 * <br/>Copyright (C), 2008-2009, FeiGao
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:TestArray.java
 * <br/>Date:2009-07-27
 * @author  FeiGao gaofeitop@gmail.com
 * @version  1.0
 */
public class TestArray{
    public static void main(String[] args){
        // 定义一个int数组类型的变量，变量名为intArr.
        int[] intArr;
        
        // 使用静态初始化，初始化数组时只指定数组元素的初始值，不指定数组长度。
        intArr = new int[]{5, 6, 8, 20};
        
        for(int a = 0; a < intArr.length; a ++){
            System.out.print(intArr[a] + "\t");
        }
        System.out.println();
        
        // 定义一个Object数组类型的变量，变量名为objArr.
        Object[] objArr;
        
        // 使用静态初始化，初始化数组时数组元素的类型是定义数组时数组元素类型的子类
        objArr = new String[]{"Java","高飞"}; 
        
        for(int b = 0; b < objArr.length; b ++){
            System.out.print(objArr[b] + "\t");
        }
        System.out.println();
        Object[] objArr2;
        
        // 使用静态初始化
        objArr2 = new Object[]{"Java","高飞"};
        
        // 数组的定义和初始化同时完成，使用动态初始化语法
        int[] prices = new int[5];
        
        // 数组的定义和初始化同时完成，初始化数组时元素的类型是定义数组时元素类型的子类。
        Object[] books = new String[4];
        
        // 输出objArr2数组中的第二个元素，将输出字符串“高飞”
        System.out.println(objArr2[1]);
        
        // 为objArr2的第一个元素赋值
        objArr2[0] = "Spring";
        
        // 输出objArr2数组中的第一个元素，将输出字符串“Spring”
        System.out.println(objArr2[0]);
        
        // 访问数组元素指定的索引等于数组长度，将出现异常
        // System.out.println(objArr2[2]);
        
        
        // 使用循环输出prices数组的每个数组元素的值。
        for (int i = 0; i < prices.length; i++) {
        	// int类型数组中每个元素的默认值都是0
        	System.out.println(prices[i]);
        }
        
        // 对动态初始化后的数组元素进行赋值
        books[0] = "Struts2权威指南";
        books[1] = "轻量级J2EE企业应用实战";
        
        // 使用循环输出books数组的每个数组元素的值
        for (int i = 0; i < books.length; i ++) {
        	// String类型数组中每个元素的默认值都是null
        	System.out.println(books[i]);
        }
    }
}
