public class Amoeba extends Shape {

    private Amoeba() { //无参数构造器
    }

    private Amoeba(String name) { //单参数构造器
        this.setName(name); //调用父类方法
    }

    /*
     * 以下要覆盖父类的两个方法必须要和父类一样设置成protected类型，否则无法覆盖。private不能访问，public不安全
     * */
    protected void rotate() {
        System.out.println("这是Amoeba类自身的rotate方法。");
    }

    protected void playSound() {
        System.out.println("这是Amoeba类自身的playSound方法。");
    }

    public static void main(String args[]) {
        Amoeba AmoebaInstance = new Amoeba("变形虫");
        AmoebaInstance.rotate();
        AmoebaInstance.playSound();
    }
}
