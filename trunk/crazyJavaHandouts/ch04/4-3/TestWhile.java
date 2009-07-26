/**
 * P 78
 * while循环
 */
public class TestWhile{
    public static void main(String[] args){
        //循环的初始化条件
        int count = 0;
        //当count小于10时，执行循环体
        while (count < 10){
            System.out.println(count);
            //迭代语句
            count ++;
        }
        System.out.println("循环结束！");

        count = 0;
        while (count < 10){
            System.out.println("不停地执行死循环" + count);
            count --;
        }
        System.out.println("永远无法跳出的循环体");

        count = 0;
        while (count < 10);//在这里出现死循环
        //下面的执行体将永远不会被执行
        {
            System.out.println(count);
            //迭代语句
            count ++;
        }
    }
}
