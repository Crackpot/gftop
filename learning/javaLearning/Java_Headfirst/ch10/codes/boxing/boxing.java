import java.util.*;
public class boxing {
    public static void main(String[] args) {
        /*
         * 包装值
         * */
        int i = 288;
        Integer iWrap = new Integer(i);//传入primitive主数据类型给包装类的构造函数。
        System.out.println(iWrap);
        /*
         * 解开包装
         * */
        int iUnWrapped = iWrap.intValue();
        System.out.println(iUnWrapped);
    }
}

/*
 * primitive主数据类型的名称：
 *     Boolean
 *     Character
 *     Byte
 *     Short
 *     Integer
 *     Long
 *     Float
 *     Doubl
 * */
