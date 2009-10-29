public class Foo {
    /*
     * 声明并初始化静态变量
     * */
    public static final int FOO_X = 25;

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Foo FooInstance = new Foo();
        System.out.println("静态变量的值为：" + FOO_X);//静态方法中直接访问静态变量
        System.out.println("静态变量的值为：" + FooInstance.FOO_X);
    }

}
