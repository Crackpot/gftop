import java.lang.Math;

/*
 * 程序运行时先进行静态处理，然后执行main函数中的语句，再执行对象构造器中的语句。
 * */
class StaticSuper {
    static {
        System.out.println("super static block");
    }
    StaticSuper() {
        System.out.println("super constructor");
    }
}
public class StaticTests extends StaticSuper {
    static int rand;
    static {
        rand = (int) (Math.random() * 6);
        System.out.println("static block " + rand);
    }
    StaticTests() {
        System.out.println("constructor");
    }
    public static void main(String[] args) {
        System.out.println("in main");
        StaticTests st = new StaticTests();
    }
}
