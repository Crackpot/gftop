import java.lang.Math;
public class Bar {
    //声明了静态变量
    public static final double BAR_SIGN;

    /*
     * 此代码块会在该类被加载时执行
     * */
    static {
        BAR_SIGN = (double)Math.random();
    }
    public static void main(String[] args) {
        Bar BarInstance = new Bar();
        System.out.println("静态变量的值为：" + BAR_SIGN);//静态方法中直接访问静态变量
        System.out.println("静态变量的值为：" + BarInstance.BAR_SIGN);
    }
}
