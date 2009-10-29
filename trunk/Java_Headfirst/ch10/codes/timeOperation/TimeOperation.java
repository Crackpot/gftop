import java.util.Date;
import java.util.Calendar;
import java.util.TimeZone;
import java.util.Locale;

public class TimeOperation {
    public static void main(String[] args) {
        Date today = new Date();
        TimeZone tz = TimeZone.getTimeZone("Asia/Shanghai");
        /*
         * java.util.Calendar 是抽象的；无法对其进行实例化。但是我们可以取得它的具体子类的实例
         * Calendar cal = new Calendar();
         * 要用这个静态的方法：
         * */
        Calendar cal = Calendar.getInstance(tz, Locale.CHINA);// 这个语法看起来很熟悉，是一个对静态方法的调用。
        System.out.println("时区为 =>\t " + cal.getTimeZone());

        System.out.println("现在时间为 =>\t " + cal.getTime());

        cal.set(2004, 0, 7, 15, 40);// 将时间设定为2004年1月7日15:40，月份从0开始
        System.out.println("设置时间为 =>\t " + cal.getTime());

        long day1 = cal.getTimeInMillis();// 将日期时间转换成以millisecond表示
        day1 += 1000 * 60 * 60;
        cal.setTimeInMillis(day1);//将cal的时间加上1个小时
        System.out.println("新的小时为 =>\t " + cal.get(cal.HOUR_OF_DAY));

        cal.add(cal.DATE, 35);
        System.out.println("加了35天 =>\t " + cal.getTime());

        cal.roll(cal.DATE, 35);// 滚动35天。注意：只有日期字段会动，月份不会动。
        System.out.println("滚动35天 =>\t " + cal.getTime());

        cal.set(cal.DATE, 1);
        System.out.println("设置为1号 =>\t " + cal.getTime());
    }
}
/*
 * Calendar API的精华
 *      重要的方法：
 *          add (int field, int amount)
 *              加减时间值
 *          get (int field)
 *              取出指定字段的值
 *          getInstance()
 *              返回Calendar，可指定地区
 *          getTimeInMillis()
 *              以毫秒返回时间
 *          roll(int field, boolean up)
 *              加减时间值，不进位
 *          set(int field,int value)
 *              设定指定字段的值
 *          set(year, month, day, hour, minute)
 *              设定完整的时间
 *          setTimeInMillis(long millis)
 *              以毫秒指定时间
 *      关键字段：
 *          DATE / DAY_OF_MONTH
 *              每月的几号
 *          HOUR / HOUR_OF_DAY
 *              小时
 *          MILLISECOND
 *              毫秒
 *          MINUTE
 *              分钟
 *          MONTH
 *              月份
 *          YEAR
 *              年份
 *          ZONE_OFFSET
 *              时区位移
 * */
