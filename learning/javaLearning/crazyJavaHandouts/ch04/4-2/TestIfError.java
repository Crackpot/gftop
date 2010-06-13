/**
 * P 74
 * 一个不能得到预期结果的if else语句
 */
public class TestIfError{
    public static void main(String[] args){
        int age = 45;
        System.out.println("年龄：" + age);
        //第一种错误的写法
        if (age > 20){
            System.out.println("青年人");
        }
        else if (age > 40){
            System.out.println("中年人");
        }
        else if (age > 60){
            System.out.println("老年人");
        }
        //第二种错误的写法
        if (age >20){
            System.out.println("青年人");
        }
        else if (age > 40 && !(age > 20)){//此种条件永远无法满足
            System.out.println("中年人");
        }
        else if (age > 60 && !(age > 20) && (age >40 && !(age > 20))){//更不可能发生
            System.out.println("老年人");
        }
        //把条件调转下，从高到低就能够达到预期结果
        if (age >60){
            System.out.println("老年人");
        }
        else if (age > 40){
            System.out.println("中年人");
        }
        else if (age >20){
            System.out.println("青年人");
        }
        //另外一种正确的写法
        if (age > 60){
            System.out.println("老年人");
        }
        else if (age > 40 && !(age > 60)){
            System.out.println("中年人");
        }
        else if (age > 20 && !(age > 40 && !(age > 60))){
            System.out.println("青年人");
        }
    }
}
