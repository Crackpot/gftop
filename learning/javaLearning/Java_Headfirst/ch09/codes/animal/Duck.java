public class Duck extends Animal {

    /*
     * 实例变量
     * */
    int size;

    /*
     * 构造函数
     * */
    public Duck() {
    }
    public Duck(int newSize) {
        super();//调用父类的构造函数
        size = newSize;
        System.out.println("Making a Duck.");
        //super();//颠倒位置，看可以编译成功么？
        
        /*
         * ./Duck.java:17: 对 super 的调用必须是构造函数中的第一个语句
         * super();//颠倒位置，看可以编译成功么？
         * ^
         * 1 错误
         * */
    }
}
