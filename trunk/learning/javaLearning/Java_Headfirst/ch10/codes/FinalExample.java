public final class FinalExample {
    final int size = 3;//size将无法改变
    final int whuffie = 43;//没有初始化将无法编译！
    static {
        /*
         * 无法为最终变量 whuffie 指定值 
         * */
        //this.whuffie = 43;
    }

    void Foof() {
        /*
         * 无法为最终变量 whuffie 指定值
         * */
        //whuffie = 42;//whuffie不能改变
    }

    void doStuff(final int x) {
        //不能改变x
    }
    void doMore() {
        final int z = 7;
        //不能改变z
    }
    public static void main(String[] args) {
        FinalExample FinalExampleInstance = new FinalExample();
    }
}

/*
 * 无法从最终 FinalExample 进行继承
 * */
//class child extends FinalExample {}
