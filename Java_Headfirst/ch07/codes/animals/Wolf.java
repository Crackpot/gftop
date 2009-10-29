public class Wolf extends Canine { //狼继承于犬科动物

    /*
     * 构造器
     * */
    protected Wolf() {
    }

    protected Wolf(String name) {
        super(name);
        //this.setName(name);
    }

    /*
     * 覆盖父类方法
     * */
    protected void makeNoise() {
        System.out.println(this.name + "发出狼叫声");
    }

    protected void eat() {
        System.out.println(this.name + "吃肉");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Wolf WolfInstance = new Wolf("狼");
        WolfInstance.makeNoise();
        WolfInstance.eat();
        WolfInstance.roam();
        WolfInstance.sleep();
    }
}
