/**
 * P 84
 * 使用break结束循环
 */
public class TestBreak{
	public static void main(String[] args){
		//一个简单的for循环
        for (int n = 0 ; n < 10 ; n ++){
            System.out.println("n的值为：" + n);
            if (n == 7){
                //执行该语句将结束循环
                break;
            }
        }
        System.out.println("break语句使得循环结束");

        outer:
        for (int i = 0 ; i < 10 ; i ++){
            for (int j = 0 ; j < 10 ; j ++){
                System.out.println("i的值为：" + i + "\t" + "j的值为：" + j);
                if (j == 3){
                    //跳出outer标签所标识的循环
                    break outer;
                }
            }
            System.out.println("这句不会被执行");
        }
        System.out.println("break语句执行，跳出outer标签所标识的循环");
    }
}
