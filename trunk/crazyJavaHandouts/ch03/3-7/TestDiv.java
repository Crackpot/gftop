/**
 * P 59
 * 除法
 */
public class TestDiv{
    public static void main(String[] args){
        double a = 5.2;
        System.out.println(a);
        double b = 3.1;
        System.out.println(b);
        double div = a / b;
        //divd的值将是1.6774193548387097
        System.out.println(div);
        //输出正无穷大:Infinity
        System.out.println("5除以0.0的结果是：" + 5 / 0.0);
        //输出负无穷大:Infinity
        System.out.println("-5除以0.0的结果是：" + -5 / 0.0);
        //下面的代码将出现异常 java.lang.ArithmeticException: / by zero
        System.out.println("-5除以0的结果是：" + -5 / 0);
    }
}
