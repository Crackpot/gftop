public class Cat extends Feline { //猫继承于猫科动物

    /*
     * 构造器
     * */
    protected Cat() {
    }
    protected Cat(String name) {
        super(name);
        //this.setName(name);
    }

    /*
     * 覆盖父类方法
     * */
    protected void makeNoise() {
        System.out.println(this.name + "发出喵喵的叫声");
    }

    protected void eat() {
        System.out.println(this.name + "吃肉，也吃素");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Cat CatInstance = new Cat("猫");
        CatInstance.makeNoise();
        CatInstance.eat();
        CatInstance.roam();
        CatInstance.sleep();
    }
}
