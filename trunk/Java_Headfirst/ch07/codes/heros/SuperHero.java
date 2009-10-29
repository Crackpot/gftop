public class SuperHero { //父类

    private String name;            /* 名称 */
    private String suit;            /* 套装 */
    private String tights;          /* 紧身衣裤 */
    private String specialPower;    /* 特殊技能 */
    
    protected void setName(String name) {
        this.name = name;
    }

    protected void useSpecialPower() {
        System.out.println(this.name + "使用特殊技能");
    }

    protected void putOnSuit() {
        System.out.println(this.name + "着装完毕");
    }
}
