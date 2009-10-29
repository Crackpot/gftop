public class Dog extends Canine { //狗继承于犬类动物

    /*
     * 构造器
     * */
    protected Dog() {
    };

    protected Dog(String name) { //在实现多态时发现类型为private时无法访问，故改成protected。
        super(name);
        //this.setName(name);
    };

    /*
     * 覆盖父类方法
     * */
    protected void makeNoise() {
        System.out.println(this.name + "发出汪汪的叫声");
    }

    protected void eat () {
        System.out.println(this.name + "肉食素食都吃");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Dog DogInstance = new Dog("狗");
        DogInstance.makeNoise();
        DogInstance.eat();
        DogInstance.roam();
        DogInstance.sleep();
    }
}
