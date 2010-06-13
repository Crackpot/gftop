public class Washer {
    Laundry laundry = new Laundry();//调用了外部的类
    /*
     * 把method声明成跟有风险的调用一样会抛出相同的异常。
     * */
    public void foo() throws ClothingException {// 有声明会抛出异常，但没有try/catch块，所以就会duck(躲避)掉，异常留给调用方
        laundry.doLaundry("DressShirt");
        /*
        try {// 把有风险的调用包在try/catch块中。
            laundry.doLaundry("DressShirt");
        } catch (ClothingException cex) {// 这随好能处理掉所有doLaundry()可能抛出的异常，不然编译器还是会包错。
            System.out.println("捕获ClothingException");
        }
        */
    }
    public static void main(String[] args) throws ClothingException {// 躲避异常
        Washer a = new Washer();
        a.foo();
    }
}
/*
 * 躲避异常会发生的事情:
 *     1 抛出ClothingException。
 *         doLaundry
 *         foo
 *         main
 *       main()调用foo()，foo()调用doLaundry()。doLaundry()抛出ClothingException。
 *
 *     2 foo()已经duck掉异常。
 *         foo
 *         main
 *       doLaundry()从stack上被取走。异常跑给foo()。
 *
 *     3 连main()也duck掉异常。
 *         main
 *       foo()也被取走…… 最后只剩下Java虚拟机，它对异常是没有什么责任感的。
 *
 *     4 Java虚拟机只好死给你看。
 * */
