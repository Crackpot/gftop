class GoodDogTestDrive {

    public static void main(String[] args) {

        GoodDog one = new GoodDog();
        one.setSize(70);
        System.out.println("Dog one: " + one.getSize());
        one.bark();

        GoodDog two = new GoodDog();
        two.setSize(8);
        System.out.println("Dog two: " + two.getSize());
        two.bark();
    }
}
