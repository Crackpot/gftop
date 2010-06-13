/**
 * P 85
 * 使用continue结束本次循环
 */
public class TestContinue{
    public static void main(String[] args){
        for (int n = 0 ; n < 10 ; n ++){
            if (n % 2 == 0){
                //跳出本次循环，继续下一次循环
                continue;
            }
            System.out.print(n + "\t");
        }
        System.out.println();

        //-----------------------------//
        //外层循环
        outer:
        for (int i = 0 ; i < 5 ; i ++){
            //内层循环
            for (int j = 0 ; j < 3 ; j ++){
                System.out.println("i的值为：" + i + "\t" + "j的值为：" + j);
                if (j == 1){
                    //跳出outer标签标识的循环
                    continue outer;
                }
            }
        }
    }
}
