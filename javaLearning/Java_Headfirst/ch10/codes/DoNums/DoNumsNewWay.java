import java.util.ArrayList;

/*
 * 自动装箱：
 *     不必把primitive主数据类型与对象分得那么清楚
 * */
public class DoNumsNewWay {
    public static void main(String[] args) {
        /*
         * ArrayList<int> listOfNumbers = new ArrayList<int>();
         * 不用以上方式声明的原因：
         *     generic类型的规则是你只能指定类或接口类型。因此ArrayList<int>将无法通过编译。但你可以直接把该包装所对应的primitive主数据类型放进ArrayList中。例如说boolean类型的放入ArrayList<Boolean>中，chars类型放入ArrayList<Character>中。
         * */
        ArrayList<Integer> listOfNumbers = new ArrayList<Integer>();//创建Integer类型的ArrayList。
        ArrayList<Boolean> listOfBooleans = new ArrayList<Boolean>();
        ArrayList<Character> listOfCharacters = new ArrayList<Character>();
        ArrayList<Byte> listOfBytes = new ArrayList<Byte>();
        ArrayList<Short> listOfShorts = new ArrayList<Short>();
        ArrayList<Long> listOfLongs = new ArrayList<Long>();
        ArrayList<Float> listOfFloats = new ArrayList<Float>();
        ArrayList<Double> listOfDoubles = new ArrayList<Double>();

        /*
         * 虽然ArrayList没有add(int)这样的方法，但编译器会自动帮你包装。
         * */
        listOfNumbers.add(3);// 直接加入项
        listOfBooleans.add(true);
        listOfCharacters.add('C');
        byte b = 1;
        listOfBytes.add(b);//我不会添加byte类型值了
        short sh = 123;
        listOfShorts.add(sh);
        listOfLongs.add(1111111111111111111L);
        float fl = 2;
        listOfFloats.add(fl);
        listOfDoubles.add(2.345);

        int num = listOfNumbers.get(0);// 编译器也会自动地解开Integer对象的包装，因此可以直接赋值给int。
        boolean booleans = listOfBooleans.get(0);
        Character chars = listOfCharacters.get(0);
        byte bytes = listOfBytes.get(0);
        short shorts = listOfShorts.get(0);
        long longs = listOfLongs.get(0);
        float floats = listOfFloats.get(0);
        double doubles = listOfDoubles.get(0);

        System.out.println("int类型值：" + num);
        System.out.println("boolean类型值：" + booleans);
        System.out.println("chars类型值：" + chars);
        System.out.println("byte类型值：" + bytes);
        System.out.println("short类型值：" + shorts);
        System.out.println("long类型值：" + longs);
        System.out.println("float类型值：" + floats);
        System.out.println("double类型值：" + doubles);
    }
}
