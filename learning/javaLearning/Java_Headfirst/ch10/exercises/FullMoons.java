import java.util.*;
import static java.lang.System.out;

/*
 * 程序的目的是要以29.52的周期计算满月，上一次的满月是在2004年1月7日。
 * */
class FullMoons {
    static int DAY_IM = 1000 * 60 * 60 * 24;// 1000是毫秒
    public static void main(String[] args) {
        Calendar c = Calendar.getInstance();// 抽象类，无法实例化
        System.out.println("现在时间为 \t" + c.getTime());
        c.set(2004, 0, 7, 15, 40);// 设置时间和数组下标类似，从0开始。0对应Jan。
        long day1 = c.getTimeInMillis();
        for (int x = 0; x < 60; x++) {
            day1 += (DAY_IM * 29.52);
            c.setTimeInMillis(day1);
            out.println(String.format("full moon on %tc", c));
        }

    }
}
