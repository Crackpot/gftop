public class RoboDog extends Robot implements Pet {
    /*
     * 构造方法
     * */
    protected RoboDog() {
    }
    protected RoboDog(String name) {
        super(name);
        //this.setName(name);
    }
    /*
     * 覆盖接口方法
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
        RoboDog RoboDogInstance = new RoboDog("机器狗");
        RoboDogInstance.beFriendly();
        RoboDogInstance.play();
    }
}
