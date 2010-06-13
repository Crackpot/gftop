public class Hippo extends Animal {
    /*
     * 1.HippoTestDrive执行new Hippo()的动作，Hippo()的构造函数进入堆栈最上方的堆栈块。
     * 2.Hippo()调用父类的构造函数导致Animal()的构造函数进入栈顶。
     * */
    public Hippo() {
        System.out.println("Making a Hippo.");
    }
    public Hippo(String name) {
        super(name);//直接将构造函数中取得的参数传递给父类的构造函数中。
        System.out.println("Making a Hippo.");
    }
}
