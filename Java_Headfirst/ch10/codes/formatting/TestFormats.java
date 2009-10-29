import java.util.Date;
/*
 * "格式化说明"的格式：
 *     根在百分号后面包括类型指示(如d或f)的每个东西都是格式化指令。除非遇到新的百分号。在类型指示之后的一组字符，格式化程序会假设都是直接输出的字符串。
 *     格式化说明最多会有5个部分(不包括%符号)。
 *     % [argument number] [flags] [width] [.precision] type
 *               1            2       3          4        5
 *     1:  如果要格式化的参数超过一个以上，可以在这里指定是哪一个。
 *     2:  特定类型的特定选项。例如数字要加逗号或正负号。
 *     3:  最小的字符数，注意：这不是总数，输出可以超过此宽度。若不足则会主动补零。
 *     4:  精确度，注意前面有个圆点符号。
 *     5:  一定要指定的类型标识。
 * */
public class TestFormats {
    public static void main(String[] args) {
        String[] str = new String[15];

        /*
         * "%,d"
         *     格式设定，用来表示应用哪种形式来输出。这里的都好是表示数字要以逗号来分开，并不是说这里有%与d两项参数。
         * 1000000000
         *     这是要格式化的数字
         * */
        str[0] = String.format("%,d",1000000000);//将输出1,000,000,000
        System.out.println(str[0]);

        /*
         * %符号代表把参数放在这里
         *     format()方法的第一个参数被成为"格式化串"，它可以带有实际上就是要这么输出而不用转译的字符。当看到%符号时，要把它想做是会被方法其余参数替换掉的位置。
         * */
        str[1] = String.format("I have %.2f bugs to fix.",476578.09876);
        System.out.println(str[1]);

        str[2] = String.format("I have %,.2f bugs to fix.",476578.09876);// 加上逗号
        System.out.println(str[2]);

        str[3] = String.format("I have %.2f, bugs to fix.",476578.09876);// 更改逗号的位置
        System.out.println(str[3]);

        System.out.println(String.format("%d",42));// 参数必须能够与int相容

        System.out.println(String.format("%.3f",42.000000));// 3配上f会强制输出3位的小数

        System.out.println(String.format("%x",42));// 十六进制，参数必须是byte、short、int、long、BigInteger

        System.out.println(String.format("%c",42));// character类型，参数为数字时为ASCII码。

        /*
         * 有许多重载版format()来取用不同数目排列组合的参数。为了应付格式化的API，Java需要一种新的功能－－称之为可变参数列表(varable argument list，简称为vararg)。
         * */
        int one = 20456654;
        double two = 100567890.246809;
        str[4] = String.format("The rank is %,d out of %,.2f",one, two);// 一项以上的参数会依序对应到格式化设定。
        System.out.println(str[4]);

        /*
         * 完整的日期与时间     %tc
         * 星期六 九月 26 01:24:33 CST 2009
         * */
        str[5] = String.format("%tc", new Date());
        System.out.println(str[5]);
        
        /*
         * 只有时间     %tr
         * 01:24:33 上午
         * */
        str[6] = String.format("%tr", new Date());
        System.out.println(str[6]);

        /*
         * 周、月、日   %tA %tB %td
         * 星期六, 九月 26
         * */
        Date today = new Date();
        str[7] = String.format("%tA, %tB %td",today, today, today);// 这样就得把Date对象传进去3次
        System.out.println(str[7]);

        /*
         * "<"这个符号是个特殊的指示，用来告诉格式化程序重复利用之前用过的参数。
         * */
        str[8] = String.format("%tA, %<tB %<td",today);//同上，但不用重复给参数
        System.out.println(str[8]);
    }
}
