import java.lang.Math;

public class MathExamples {
    public static void main(String[] args) {
        MathExamples MathExamplesInstance = new MathExamples();
        System.out.println("系统随机产生的数字是：" + Math.random());
        System.out.println("-240.45 的绝对值为：" + Math.abs(-240.45));
        System.out.println("-240.55 圆整之后的结果为：" + Math.round(-240.55));
        System.out.println("-240.55 取整之后的结果为：" + (int)(-240.55));
        System.out.println("24与240中的最小值为：" + Math.min(24, 240));//两个参数
        System.out.println("24与240中的最大值为：" + Math.max(24, 240));//两个参数
    }
}
