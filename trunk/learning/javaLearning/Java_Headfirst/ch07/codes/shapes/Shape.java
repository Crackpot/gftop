public class Shape { // 父类

    private String name;

    /*
     * 以下被子类调用的方法绝对不能设置为private类型
     * */
    protected void setName(String name) { // 在各个子类的构造器中调用此方法来设置名称
        this.name = name;
    }

    protected void rotate() {
        System.out.println(this.name + "执行rotate动作");
    }

    protected void playSound() {
        System.out.println(this.name + "执行playSound动作");
    }
}
