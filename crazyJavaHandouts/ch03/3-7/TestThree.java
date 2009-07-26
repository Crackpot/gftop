/**
 * P 68
 * 三目运算符
 */
public class TestThree{
    public static void main(String[] args){
        String str = 5 > 3 ? "5大于3" : "5不大于3";
        System.out.println(str);
        //将上面的写法转换成if else写法：
        String str2 = null;
        if (5 > 3) {
            str2 = "5大于3";
        }
        else {
            str2 = "5不大于3";
        }
        System.out.println(str2);
    }
}
