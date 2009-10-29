public class Hippo extends Animal { //河马类，暂不明属种，单独继承于Animal

    /*
     * 构造器
     * */
    protected Hippo() {
    }

    protected Hippo(String name) {
        super(name);
        //this.name = name;
    }

    /*
     * 覆盖父类方法
     * */
    protected void makeNoise() {
        System.out.println(this.name + "发出河马叫声");
    }

    protected void eat() {
        System.out.println(this.name + "吃素");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Hippo HippoInstance = new Hippo("河马");
        HippoInstance.makeNoise();
        HippoInstance.eat();
        HippoInstance.roam();
        HippoInstance.sleep();
    }
}
