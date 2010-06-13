public class Tiger extends Feline { //老虎类继承于猫科动物类

    /*
     * 构造器
     * */
    protected Tiger() {
    }

    protected Tiger(String name) {
        super(name);
        //this.setName(name);
    }

    /*
     * 覆盖父类方法
     * */
    protected void makeNoise() {
        System.out.println(this.name + "发出老虎吼声");
    }
    protected void eat() {
        System.out.println(this.name + "吃肉");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Tiger TigerInstance = new Tiger("老虎");
        TigerInstance.makeNoise();
        TigerInstance.eat();
        TigerInstance.roam();
        TigerInstance.sleep();
    }
}
