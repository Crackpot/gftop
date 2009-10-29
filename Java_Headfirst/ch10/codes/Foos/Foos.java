class Foo {
    static int x;
    public void go() {
        System.out.println(x);//将输出0，默认值为0
    }
}

class Foo2 {
    int x;
    public static void go() {
        /*
         * 无法从静态上下文中引用非静态 变量 x
         * */
        //System.out.println(x);
    }
}

class Foo3 {
    /*
     * 可能尚未初始化变量 x
     * */
    //final int x;
    int x;

    public void go() {
        System.out.println(x);
    }
}

class Foo4 {
    static final int x = 12;
    public void go() {
        System.out.println(x);//非静态可以访问静态
    }
}

class Foo5 {
    static final int x = 12;
    public void go(final int x) {
        System.out.println(x);
    }
}


class Foo6 {
    int x = 12;
    public static void go(final int x) {
        System.out.println(x);
    }
}

public class Foos {
    public static void main(String[] args) {
        Foos FoosInstance = new Foos();

        Foo FooInstance = new Foo();
        FooInstance.go();//无法从静态上下文中引用非静态 方法 go()

        Foo2 Foo2Instance = new Foo2();
        Foo2Instance.go();

        Foo3 Foo3Instance = new Foo3();
        Foo3Instance.go();

        Foo4 Foo4Instance = new Foo4();
        Foo4Instance.go();

        Foo5 Foo5Instance = new Foo5();
        Foo5Instance.go(13);

        Foo6 Foo6Instance = new Foo6();
        Foo6Instance.go(13);
    }
}
