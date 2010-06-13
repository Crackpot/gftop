/**
 * P 81
 * for循环错误的实例
 */
public class TestForError{
    public static void main(String[] args){
        //循环的初始化条件，循环条件，循环迭代语句都在下面一行
        for(int count = 0 ; count < 10 ; count ++){
            System.out.println(count);
            //再次修改了循环变量
            count *= 0.1;
        }
    }
}
