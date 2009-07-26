/**
 * P 67
 * 逻辑运算符
 */
public class TestLogicOperator{
    public static void main(String[] args){
        //直接对false求非运算，将返回true
        System.out.println(!false);
        System.out.println(5 > 3 && '6' > 10);
        System.out.println(2 > 3 || 'c' > 'a');
        System.out.println(2 > 3 ^ 'c' > 'a');//两个不同的操作数异或返回true
        System.out.println(5 > 3 ^ '6' > 10);//两个相同的操作数异或返回false
        /**
         * 关于或运算：
         * 1、"|" 不短路或 总是执行两个操作数
         * 2、"||" 短路或 如果第一个操作数返回true，它将不再对第二个操作数求值，直接返回true
         */
        int a = 5;
        int b = 10;
        if (a > 4 | b++ > 10){
            //输出a的值为5，b的值为11
            System.out.println("a的值为：" + a + "\t" + "b的值为：" + b);
        }
        int c = 5;
        int d = 10;
        if (c > 4 || d++ > 10){
            //输出c的值为5，d的值为10
            System.out.println("c的值为：" + c + "\t" + "d的值为：" + d);
        }
    }
}
