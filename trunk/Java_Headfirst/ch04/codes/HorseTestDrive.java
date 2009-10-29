class HorseTestDrive {
    public static void main(String[] args) {
        Horse horse = new Horse();
        //horse.setBreed("BreedValue");// 实例变量不进行初始化也可以编译
        System.out.println("The height of the horse is " + horse.getHeight());
        System.out.println("The breed of the horse is " + horse.getBreed());
    }
}
