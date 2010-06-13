/**
 * P 79
 * do while实例
 */
public class TestDoWhile{
    public static void main(String[] args){
        int count = 1;
        //执行do循环
        do{
            System.out.println(count);
            //循环迭代语句
            count ++;
        }
        //循环条件紧跟while关键字
        while(count < 10);
        System.out.println("循环结束");
    }
}
