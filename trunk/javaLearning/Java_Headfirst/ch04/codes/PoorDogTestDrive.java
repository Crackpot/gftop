public class PoorDogTestDrive {
    public static void main(String[] args) {
        PoorDog one = new PoorDog();

        // 无需初始实例变量，因为它们含有默认值
        System.out.println("Dog size is " + one.getSize());
        System.out.println("Dog name is " + one.getName());
    }
}
