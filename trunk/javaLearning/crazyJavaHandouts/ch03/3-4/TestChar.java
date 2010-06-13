public class TestChar{
    public static void main(String[] args){
        //直接指定耽搁字符作为字符常量
        char aChar = 'a';
        System.out.println(aChar);
        char enterChar = '\r';
        System.out.println(enterChar);
        //使用Unicode编码值来指定字符常量
        char ch = '\u9999';     //将输出一个'香'字符
        System.out.println(ch);
        char zhong = '中';      //定义一个'中'字符变量
        //直接将一个char变量当成int类型变量使用    
        int zhongValue = zhong;
        System.out.println(zhong);
        System.out.println(zhongValue);
        //直接将一个0~65535范围内的int整数赋给一个char变量
        char c = 97;
        System.out.println(c);
        //Java没有提供表示字符串的基本数据类型，而是通过String类来表示字符串。
        String s = "海上升明月，天涯共此时";
        System.out.println(s);   
    }
}