public abstract class Animal { 
    
    /* 继承下去的方法可以被子类覆盖，但实例变量则不会 */

    /*
     * 实例变量
     * */
    protected String name;          /* 名称，在子类中要直接访问，改为protected类型 */
    private String picture;         /* 图片 */
    private String food;            /* 食物 */
    private boolean hunger;         /* 饥饿否 */
    private String boundaries;      /* 边界，分界线 */
    private String location;        /* 位置 */

    /*
     * 构造函数
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

/*
 * 本章要点：
 *
 *     如果不想让某个类被初始化，就以abstract这个关键词将它标记为抽象的。
 *     抽象的类可以带有抽象的和非抽象的方法。
 *     如果类带有抽象的方法，则此类必定标识为抽象的。
 *     抽象的方法没有内容，它的声明以分号结束。
 *     抽象的方法必须要在具体的类中运行。
 *     Java所有的类都是Object(java.lang.Object)直接或间接的子类。
 *     方法可以访问Object的参数或返回类型。
 *     不管实际上所引用的对象是什么类型，只有在引用变量的类型就是带有某方法的类型才能调用该方法。
 *     Object应用变量在没有类型转换的情况下不能赋值给其他的类型，若堆上的对象类型与所要转换的类型不兼容，则此转换会在执行期间产生异常。
 *         类型转换的例子： Dog d = (Dog) x.getObject(aDog);
 *     从ArrayList<Object>取出的对象只能被Object引用，不然就要用类型转换来改变。
 *     Java不允许多重继承，因为那样会有致命方块的问题。
 *     接口就好像是100%纯天然抽象类。
 *     以interface这个关键词取代class来声明接口。
 *     实现接口时要使用implements这个关键词。
 *         例如： Dog implements Pet
 *     class可以实现多个接口。
 *     实现某接口的类必须实现它所有的方法，因为这些方法都是public与abstract的。
 *     要从子类调用父类的方法可以用super这个关键词来引用。
 *         例如： super.runReport();
 * */
