public class MyAnimalListTestDrive {

    public static void check(Animal a) {
        /*
         * Object类含有的方法
         * */
        if (a.equals(a)) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }

        System.out.println(a.getClass());
        System.out.println(a.hashCode());
        System.out.println(a.toString());
        System.out.println();
    }

    public static void main(String[] args) {
        MyAnimalList list = new MyAnimalList();
        Dog a = new Dog();
        Hippo b = new Hippo();
        Cat c = new Cat();
        list.add(a);
        check(a);
        list.add(b);
        check(b);
        list.add(c);
        check(c);
    }
}
