class MyEx extends Exception {
    // 自定义的异常类
}// close class MyEx
public class ExTestDrive {
    static void doRisky(String t) throws MyEx {
        System.out.print("h");
        if ("yes".equals(t)) {
            throw new MyEx();
        }
        System.out.print("r");
    }// close method doRisky
    public static void main(String[] args) {
        String test = args[0];
        //System.out.println("参数为：" + args[0]);
        try{
            System.out.print("t");
            doRisky(test);
            System.out.print("o");
        } catch(MyEx e) {
            System.out.print("a");
        } finally {
            System.out.print("w");
        }
        System.out.println("s");
    }// close method main
}// close class ExTestDrive
