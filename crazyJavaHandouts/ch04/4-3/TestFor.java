/**
 * P 81
 * for实例
 */
public class TestFor{
    public static void main(String[] args){
        System.out.println("循环1开始");
        for(int count = 0 ; count < 10 ; count ++){
            System.out.println(count);
        }
        System.out.println("循环1结束");

        System.out.println("循环2开始");
        for (int b = 0 , s = 0 , p = 0 ; b < 10 && s < 4 && p < 10 ; p++){
            System.out.println(b++);
            System.out.println(++s + p);
        }
        System.out.println("循环2结束");
    }
}
