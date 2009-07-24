public class TestFloat{
    public static void main(String[] args){
        float af = 3.1415926f;
        //下面将看到af的值发生了改变
        System.out.println(af);
        double a = 0.0;
        System.out.println(a);
        double c = Double.NEGATIVE_INFINITY;
        System.out.println(c);
        float d = Float.NEGATIVE_INFINITY;
        System.out.println(d);
        //将看到float和double的负无穷大是相等的
        System.out.println(c == d);
        //0.0除以0.0将出现非数
        System.out.println(a / a);
        //两个非数之间是不相等的
        System.out.println(a / a == Float.NaN);
        //所有正无穷大都是相等的
        System.out.println(6.0 / 0 == 555.0 / 0);
        //负数除以0.0得到负无穷大
        System.out.println(-8 / a);
        //下面这句将抛出除以0的异常
        //System.out.println(0 / 0);
    }
}
