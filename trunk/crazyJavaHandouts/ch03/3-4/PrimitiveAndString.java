public class PrimitiveAndString{
    public static void main(String[] args){
        //下面代码是错的，因为5是一个整数，不能直接赋值给一个字符串
        //String str1 = 5;
        //一个基本类型值和字符串进行连接运算时，基本类型值自动转换为字符串
        String str2 = 3.5f + "";
        //下面将输出3.5
        System.out.println(str2);
        //下面这句将输出8Hello
        System.out.println(3 + 5 + "Hello");
        //下面这句将输出Hello35，因为Hello+3将把3当成字符串处理
        System.out.println("Hello" + 3 + 5);
    }
}
