public class AutoBoxing {
    /*
     * AutoBoxing不只是包装与解开primitive主数据类型给collection用而已，它还可以让你在各种地方交换地运用primitive主数据类型与它的包装类型。
     * */

    /*
     * 方法的参数
     *     如果参数是某种包装类型，你可以转入相应的primitive主数据类型，反之亦然。
     * */
    public void takeNumber(Integer i) {
        System.out.println(i);
    }

    /*
     * 返回值
     *     如果method声明为返回某种primitive主数据类型，你也可以返回兼容的primitive主数据类型或该primitive主数据类型的包装类型。
     * */
    public int giveNumber() {
        Integer num = new Integer(333); 
        System.out.println(num);
        return num;//函数要求返回值类型为int
    }
    /*
     * Boolean表达式
     *     任何预期Boolean的值的位置都可以用求出boolean的表达式来代替，例如说4>2或者Boolean包装类型的引用。
     * */
    public void booleanTest() {
        boolean flag = true;
        if (flag || (4 > 3)) {
            System.out.println("booleanTest");
        }
    }

    /*
     * 数值运算
     *     这或许是最诡异的。你可以在使用primitive主数据类型作为运算的子操作中以包装类型来替换。这代表你可以对Integer的对象作递增运算。
     * */
    public void numericalOperation() {
        Integer i = new Integer(42);
        while (i < 45) {
            Integer j = new Integer(i.intValue());//将Integer类型转换成int类型再装箱
            Integer k = j + 3;
            System.out.println("i:" + i);
            System.out.println("k:" + k);
            i ++;
        }
    }
    /*
     * 赋值
     *     你可以将包装类型或primitive主数据类型赋给声明成相对应的包装或primitive主数据类型。
     * */
    public void evaluate (){
        int x = 3;
        Integer num = new Integer(x);
        double d = num;
        Double da = d;
        System.out.println(d);
        System.out.println(da);
    } 
    /*
     * 包装的静态实用性方法
     *     除了一般类的操作外，包装也有一组实用的静态方法。如Integer.parseInt()，这个方法取用String并返回给你primitive主数据类型值。
     * */
    public void staticMethod() {
        String s = "2";
        int x = Integer.parseInt(s);//将"2"解析成2
        System.out.println("\"2\"解析为数字的结果为：" + x);
        double d = Double.parseDouble("420.24");
        System.out.println("Double转换为double类型为：" + d);
        boolean b = new Boolean("true").booleanValue();
        System.out.println("Boolean转换为boolean类型为：" + b);
    }
    /*
     * 将primitive主数据类型值转换成String
     * */
    public void DoubleToString() {
        double d = 42.5;
        String doubleString = "" + d;// "+"这个操作数是Java中唯一有重载过的运算符
        System.out.println("转换后的doubleString为：" + doubleString);
        String doubleString2 = Double.toString(d);// 使用了Double这个类的静态方法toString()。
        System.out.println("转换后的doubleString2为：" + doubleString2);
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        AutoBoxing AutoBoxingInstance = new AutoBoxing();
        AutoBoxingInstance.takeNumber(32);
        AutoBoxingInstance.giveNumber();
        AutoBoxingInstance.booleanTest();
        AutoBoxingInstance.numericalOperation();
        AutoBoxingInstance.evaluate();
        AutoBoxingInstance.staticMethod();
        AutoBoxingInstance.DoubleToString();
    }
}
