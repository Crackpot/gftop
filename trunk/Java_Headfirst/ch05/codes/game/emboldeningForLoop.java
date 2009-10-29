public class emboldeningForLoop {
    public static void main(String[] args){
        String[] strArr = {"hello","crackpot","I","love","China"};
        for (String str : strArr) {// 以str作为名称遍历数组strArr中的所有元素
            System.out.println("String类型的数组strArr中的元素为：" + str);
        }
    }
}
