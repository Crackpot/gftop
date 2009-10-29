public class Lion extends Feline { //狮子类继承于猫科动物类

    /*
     * 构造器
     * */
    protected Lion() {
    }
    protected Lion(String name) {
        super(name);
        //this.setName(name);
        //super.eat();
    }


    /*
     * 覆盖父类方法
     * */
    protected void makeNoise() {
        System.out.println(this.name + "发出狮吼声");
    }

    protected void eat() {
        System.out.println(this.name + "吃肉");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Lion LionInstance = new Lion("狮子");
        LionInstance.makeNoise();
        LionInstance.eat();
        LionInstance.roam();
        LionInstance.sleep();
        LionInstance.setLocation("东北");
        System.out.println("位置：" + LionInstance.getLocation());
    }
}
