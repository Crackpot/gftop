public abstract class Animal {
    private String name;
    /*
     * 构造器
     * 3.Animal()调用父类的构造函数致使Object()的构造函数进入栈顶。
     * 4.Object()执行完毕，它的堆栈块被弹出，接着继续执行Animal()的。
     * */
    public Animal() {
        System.out.println("Making an Animal.");
    }
    public Animal(String theName) {
        name = theName;
        System.out.println("Making an Animal.");
    }
    /*
     * setter与getter
     * */
    public void setName(String newName) {
        name = newName;
    }
    public String getName() {
        return name;
    }
}
