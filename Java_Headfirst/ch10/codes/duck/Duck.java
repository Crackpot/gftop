import java.lang.Math;
class Ducktoy {
    //Duck() 可以在 Duck 中访问 private
    //    Duck d = new Duck();

    //Duck d = new Duck();
}

public class Duck {
    /*
     * 实例变量
     * 每个Duck对象都有自己的size变量，但所有Duck实例只有一份duckCount变量。静态变量是共享的。(两个小鬼吃一根冰棍)
     * */
    private int size;
    private static int duckCount = 0;//用静态变量来统计创建了几个对象

    /*
     * 构造器
     * 私有的构造函数代表这个类不能被本身以外的程序实例化。
     * */
    private Duck() {
        duckCount++;//每当构造函数执行的时候，此变量的值会递增。
        this.count();
        this.setSize((int)(Math.random()*100));
        System.out.println("鸭子的重量为：" + this.getSize() + "\n");
    }

    public void setSize(int s) {
        size = s;
    }
    public int getSize() {
        return size;
    }
    public void count() {
        System.out.println("创建第" + duckCount +"个鸭子对象");
    }

    public static void main(String[] args) {
        System.out.println("用静态变量来统计创建了几个对象：\n");
        Duck[] DuckInstance = new Duck[4];
        DuckInstance[0] = new Duck();
        DuckInstance[1] = new Duck();
        DuckInstance[2] = new Duck();
        DuckInstance[3] = new Duck();
    }
}
