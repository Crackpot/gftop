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
        //定义一个int数组类型的变量，变量名为intArr.
        int[] intArr;
        //使用静态初始化，初始化数组时只指定数组元素的初始值，不指定数组长度。
        intArr = new int[]{5, 6, 8, 20};
        //定义一个Object数组类型的变量，变量名为Object.
        Object[] objArr;
        //使用静态初始化，初始化数组时数组元素的类型是定义数组时数组元素类型的子类
        objArr = new String[]{"Java","高飞"}; 
    }
}
