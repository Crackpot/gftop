class YesException extends Exception {
    // 创建一个自定义异常类
}// close class YesException

class NoException extends Exception {
    // 创建一个自定义异常类
}// close class NoException

public class TestExceprions {
    public static void main(String[] args) {
        String test = "yes";// 此时会抛出YesException异常
        //String test = "no";// 此时会抛出NoException异常
        //String test = "other";// 此时不会抛出异常

        try {
            System.out.println("开始try程序块");
            doRisky(test);
            System.out.println("结束try程序块");
        } catch (YesException yex) {
            System.out.println("捕获到NoException异常");
        } catch (NoException nex) {
            System.out.println("捕获到NoException异常");
        } finally {
            System.out.println("Finally程序块");
        }
        System.out.println("main方法结束");
    }// close method main

    static void doRisky(String test) throws YesException, NoException {// 处理多重异常的静态方法
        System.out.println("risky方法开始");
        if ("yes".equals(test)) {// 如果test为yes，抛出YesException
            throw new YesException();
        } else if ("no".equals(test)) {// 如果test为no，抛出NoException
            throw new NoException();
        }
        System.out.println("risky方法结束");
        return;
    }// close method doRisky
}// close class TestExceprions
