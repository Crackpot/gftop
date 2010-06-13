public class Dog extends Canine implements Pet { //狗继承于犬类动物

    /*
     * 构造器
     * */
    protected Dog() {
    };

    protected Dog(String name) { //在实现多态时发现类型为private时无法访问，故改成protected。
        super(name);
        //this.setName(name);
    }

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
     * 覆盖接口方法
     * */
    public void beFriendly() {
        System.out.println(this.name + "和主人亲热");
    } 

    public void play() {
        System.out.println(this.name + "和主人玩耍");
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Dog DogInstance = new Dog("狗");
        DogInstance.makeNoise();
        DogInstance.eat();
        DogInstance.beFriendly();//接口方法
        DogInstance.roam();
        DogInstance.play();//接口方法
        DogInstance.sleep();
    }
}
