/**
 * P 87
 * 使用return结束方法
 */
public class TestReturn{
    public static void main(String[] args){
        for(int i = 0 ; i < 5 ; i ++){
            System.out.println("i的值为：" + i);
            if (i == 3){
                return;
            }
            System.out.println("return后的输出语句");
        }
    }
}
