/**
 * P 82
 * 用for循环替代while循环
 */
public class TestForInsteadWhile{
    public static void main(String[] args){
        //把for循环的初始化条件提出来独立定义
        int count = 0;
        //for循环里只放循环条件
        for( ; count < 10 ; ){
            System.out.println(count);
            //把循环迭代部分放在循环体之后定义
            count ++;
        }
        //此处还可以访问count变量
        System.out.println("循环变量count的值为：" + count);
        //-----------------------------------//
        int tmp = 0;
        for(int count2 = 0 ; count2 < 10 ; count2 ++){//count2之在整个for循环中起作用，放到外面就不能用了
            System.out.println(count2);
            //使用tmp来保存循环变量count2的值
            tmp = count2;
        }
        //System.out.println("循环变量count的值为：" + count2);//此句错误，找不到符号count2
        System.out.println("用变量tmp表示循环变量count的最后的值为：" + tmp);
    }
}
