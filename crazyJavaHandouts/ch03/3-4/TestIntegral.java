public class TestIntegral{
    public static void main(String[] args){
        //下面的代码是正确的，系统会自动把56当成byte类型处理
        byte a = 56;
        System.out.println(a);
        int i = 2;
        System.out.println(i);
        /**
         * 下面的代码是错误的，系统不会把9999999999999999当作long类型处理，
         * 所以超出了int的表述范围，从而引起错误。
         */
        //long bigValue = 9999999999999999;
        //下面这句是正确的，在巨大的整数常量后使用L后缀，强制使用long类型。
        long bigValue = 9999999999999999L;
        System.out.println(bigValue);
        //以0开头的整数常量是8进制的整数
        int octaValue = 013;
        System.out.println(octaValue);
        //以0x或0X开头的整数常量是16进制的整数
        int hexValue1 = 0x13;
        System.out.println(hexValue1);
        int hexValue2 = 0XaF;
        System.out.println(hexValue2);
    }
}
