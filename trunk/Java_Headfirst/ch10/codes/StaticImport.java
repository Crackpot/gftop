import static java.lang.System.out;
import static java.lang.Math.*;

public class StaticImport {
    public static void main(String[] args) {
        out.println("sqrt(2.0) = " + sqrt(2.0));
        out.println("tan(60) = " + tan(60));
    }
}
/*
 * 时机与要领
 *      如果只会用到一两次，不如不用静态的import，这样程序会比较好阅读。
 *      如果会用到很多次，或许用static import会让程序看起来比较清爽。
 *      在静态import的声明中也可以使用.*这样的通用字符。
 *      最重要的问题是容易产生名称的冲突。如add()到底是要调用哪个方法。
 * */
