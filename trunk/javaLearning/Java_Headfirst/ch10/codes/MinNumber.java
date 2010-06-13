import java.lang.Math;

public class MinNumber {
    public static int min() {
        int[] num = {0,0};
        num[0]= (int)(Math.random()*100);
        num[1]= (int)(Math.random()*100);
        // 以类的名称调用静态的方法
        // 区别于用变量的名称调用非静态的方法：
        //      SongInstance2.play();
        int min = Math.min(num[0],num[1]);
        System.out.println("系统随机生成的两个数字为：" + num[0] + "," + num[1] + "\t\t 其中较小的数字为：" + min);
        return min;
    }
    public static void displayInformation(String content) {
        System.out.println(content);
    }

    public void hello() {// 非静态方法
        System.out.println("静态方法无法调用非静态方法。");
    }
    public static void main(String[] args) {
        MinNumber MinNumberInstance = new MinNumber();
        displayInformation("静态的方法调用静态的方法"); // 直接调用静态方法
        MinNumberInstance.displayInformation("用实例来调用方法");
        min();//调用静态方法
        //hello();//无法从静态上下文中引用非静态 方法 hello()
        MinNumberInstance.hello();
    }
}
