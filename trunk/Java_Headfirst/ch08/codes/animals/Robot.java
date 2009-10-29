public abstract class Robot {

    /*
     * 实例变量
     * */
    protected String name;        /*名称*/

    /*
     * 构造器
     * */
    protected Robot() {
    }
    protected Robot(String newName) {
        this.name = newName;
        System.out.println(this.name + "是机器");
    }

    /*
     * 方法
     * */
    protected void setName(String name) { //子类会调用，故设置成为protected
        this.name = name;
    }
    protected String getName() {
        return this.name;
    }
}
