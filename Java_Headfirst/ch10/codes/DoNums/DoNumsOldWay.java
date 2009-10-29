import java.util.ArrayList;
public class DoNumsOldWay {
    public static void main(String[] args) {
        ArrayList listOfNumbers = new ArrayList();// 创建出ArrayList对象
        listOfNumbers.add(new Integer(3));// 不能直接加入primitive的3，得先转换成Integer。
        Integer one = (Integer) listOfNumbers.get(0);// 返回Object类型，但可以转换为Integer。
        int intOne = one.intValue();// 最后再取出primitive。
        System.out.println(intOne);
    }
}
