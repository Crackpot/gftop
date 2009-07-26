/**
 * P 61
 * 赋值运算符
 */
public class TestAssignOperator{
    public static void main(String[] args){
        //为变量str赋值为Java
        String str = "Java";
        System.out.println(str);
        //为变量pi赋值为3.14
        double pi = 3.14;
        System.out.println(pi);
        //为变量visited赋值为true
        boolean visited = true;
        System.out.println(visited);
        //将str的值赋给str2
        String str2 = str;
        System.out.println(str2);
        int a;
        int b;
        int c;
        //通过为a,b,c赋值，三个变量的值都是7
        //虽然Java支持这种一次为多个变量赋值的写法，但这种写法会降低程序的可读性，因此不建议这样写。
        a = b = c = 7;
        System.out.println(a + '\n' + b + '\n' + c);//此语句中会将转义字符转换为int类型参与运算
        System.out.println(a + "\n" + b + "\n" + c);//此语句会输出三个变量的值
        double d1 = 12.34;
        //将表达式的值赋给d2
        double d2 = d1 + 5;
        System.out.println(d2);
    }
} 
