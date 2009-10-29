public class Polymiorphism extends Animal{ //多态类，用来演示多态

    public static void main(String[] args) {

        Animal[] animals = new Animal[6];
        animals[0] = new Lion("狮子");
        animals[1] = new Tiger("老虎");
        animals[2] = new Cat("猫");
        animals[3] = new Hippo("河马");
        animals[4] = new Wolf("狼");
        animals[5] = new Dog("狗");

        for (int i = 0; i < animals.length; i++) {
            System.out.println();
            animals[i].eat();
            animals[i].roam();
        }
    }
}
