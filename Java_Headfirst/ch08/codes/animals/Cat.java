public class Cat extends Feline implements Pet { //猫继承于猫科动物

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
     * 覆盖接口Pet的方法
     * 接口中为public abstract void xxx() {}
     * 在这里覆盖时要去掉abstract
     * */
    public void beFriendly() {
        System.out.println(this.name + "和主人亲热");
    }
    public void play() {
        System.out.println(this.name + "和主人玩耍");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Cat CatInstance = new Cat("猫");
        CatInstance.makeNoise();
        CatInstance.eat();
        CatInstance.beFriendly();//接口方法
        CatInstance.roam();
        CatInstance.play();//接口方法
        CatInstance.sleep();
    }
}
