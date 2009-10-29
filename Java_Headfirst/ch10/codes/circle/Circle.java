import java.lang.Math;

public class Circle {
    /*
     * 静态的final变量是常数
     * 一个被标记为final的变量代表它一旦被初始化后就不会改动。也就是说该类加载之后静态final变量就一直会维持原值。
     * 常数变量的名称应该都是大写字母！
     * */
    public static final double PI = 3.141592653589793;
    public double radius;
    public double perimeter;
    public double area;
    /*
     * 构造器
     * */
    public Circle() {
        this.radius = Math.random() * 100;
        System.out.println("圆的半径为：" + this.radius);
        this.perimeter(this.radius);
        this.area(this.radius);
    }
    public Circle(double radius) {
        this.radius = radius;
        System.out.println("圆的半径为：" + this.radius);
        this.perimeter(this.radius);
        this.area(this.radius);
    }

    /*
     * 周长求算方法
     * */
    public double perimeter(double radius) {
        this.perimeter = 2 * PI * this.radius;//直接使用静态变量
        System.out.println("圆的周长为：" + this.perimeter);
        return this.perimeter;
    }
    /*
     * 面积求算方法
     * */
    public double area(double radius) {
        this.area = PI * Math.pow(this.radius,2);//直接使用静态变量
        System.out.println("圆的面积为：" + this.area);
        return this.area;
    }
    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Circle CircleInstance = new Circle();
    }
}
