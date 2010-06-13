public class Animal {
    
    /* 继承下去的方法可以被子类覆盖，但实例变量则不会 */

    /*
     * 各个实例变量
     * */
    protected String name;          /* 名称，在子类中要直接访问，改为protected类型 */
    private String picture;         /* 图片 */
    private String food;            /* 食物 */
    private boolean hunger;         /* 饥饿否 */
    private String boundaries;      /* 边界，分界线 */
    private String location;        /* 位置 */
    /*
     * 构造器
     * */
    protected Animal() {
    }
    protected Animal(String name) {
        this.name = name;
        System.out.println(this.name + "是动物");
    }

    /*
     * setter与getter，用private子类无法访问，用default会出现问题
     * */
    protected void setName(String name) {
        this.name = name;
    }
    protected String getName() {
        return this.name;
    }

    protected void setPicture(String picture) {
        this.picture = picture;
    }
    protected String getPicture() {
        return this.picture;
    }

    protected void setFood(String food) {
        this.food = food;
    }
    protected String getFood() {
        return this.food;
    }

    protected void setHunger(boolean hunger) {
        this.hunger = hunger;
    }
    protected boolean getHunger() {
        return this.hunger;
    }

    protected void setBoundaries(String boundaries) {
        this.boundaries = boundaries;
    }
    protected String getBoundaries() {
        return this.boundaries;
    }

    protected void setLocation(String location) {
        this.location = location;
    }
    protected String getLocation() {
        return this.location;
    }

    /*
     * 以下子类共有的方法都使用protected类型
     * */
    protected void makeNoise() {
        System.out.println(this.name + "发出声音");
    }
    protected void eat() {
        System.out.println(this.name + "进食");
    }
    protected void sleep() {
        System.out.println(this.name + "睡觉");
    }
    protected void roam() { //漫游，闲逛，徜徉
        System.out.println(this.name + "闲逛");
    }
}
