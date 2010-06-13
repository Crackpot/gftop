public abstract class Feline extends Animal { //猫科动物类

    /*
     * 构造函数
     * */
    protected Feline() {
    }
    protected Feline(String name) {
        super(name);
        System.out.println(this.name + "是猫科动物");
    }

    /*
     * 覆盖父类方法
     * */
    protected void roam() {
        System.out.println(this.name +"以猫科动物活动方式闲逛");
    }
}
