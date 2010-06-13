public abstract class Canine extends Animal { //犬类动物
    /*
     * 构造函数
     * */
    protected Canine() {
    }
    protected Canine(String name) {
        super(name);
        System.out.println(this.name + "是犬类动物");
    }

    /*
     * 覆盖父类方法
     * */
    protected void roam() {
        System.out.println(this.name + "以犬科动物活动方式活动");
    }
}
