public class Mushroom {
    /*
     * 构造器
     * */
    public Mushroom() {
        System.out.println("没有说明大小的蘑菇");
    }
    public Mushroom(int size) {
        System.out.println("大小为" + size +"的蘑菇");
    }
    public Mushroom(boolean isMagic) {
        if (isMagic) {
            System.out.println("不明大小的魔菇");
        } else {
            System.out.println("不明大小的一般蘑菇");
        }
    }
    public Mushroom(boolean isMagic, int size) {
        if (isMagic) {
            System.out.println("大小为" + size + "的魔菇");
        } else {
            System.out.println("大小为" + size + "的一般蘑菇");
        }
    }
    public Mushroom(int size, boolean isMagic) {
        if (isMagic) {
            System.out.println("大小为" + size + "的魔菇");
        } else {
            System.out.println("大小为" + size + "的一般蘑菇");
        }
    }
}
/*
 * 要点：
 *     实例变量保存在所属的对象中，位于堆上。
 *     如果实例变量是个对对象的引用，则引用与对象都是在堆上。
 *     构造函数是个会在新建对象的时候执行程序代码。
 *     构造函数必须与类同名且没有返回类型。
 *     可以用构造函数来初始被创建对象的状态。
 *     如果没有写构造函数，编译器会安排一个。
 *     默认的构造函数是没有参数的。
 *     如果写了构造函数，则编译器就不会调用。
 *     最好能有无参数的构造函数让人可以选择使用默认值。
 *     重载的构造函数意思是有超过一个以上的构造函数。
 *     重载的构造函数必须有不同的参数。
 *     两个构造函数的参数必须不同。
 *     实例变量有默认值，原始的默认值是0/0.0/false，引用的默认值是null。
 * */
