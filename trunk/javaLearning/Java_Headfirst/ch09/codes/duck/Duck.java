public class Duck {
    /*
     * 实例变量，存在于堆上
     * */
    private int size;
    int pounds = 6;
    float floatability = 2.1F;
    String name = "Generic";
    long[] feathers = {1, 2, 3, 4, 5, 6, 7};
    boolean canFly = true;
    int maxSpeed = 25;

    /*
     * 构造器
     * */
    public Duck() { // 没有参数的构造器
        System.out.println("type 1 duck");
    }
    public Duck(boolean fly) {
        canFly = fly;
        System.out.println("type 2 duck");
        System.out.println("canFly = " + canFly);
    }
    public Duck(String n, long[] f) {
        name = n;
        feathers = f;
        System.out.println("type 3 duck");
        System.out.print("name = " + name + "\t feathers = " + feathers + "\n");
    }
    public Duck(int w, float f) {
        pounds = w;
        floatability = f;
        System.out.println("type 4 duck");
        System.out.print("pounds = " + pounds + "\t floatability = " + floatability + "\n");
    }
    public Duck(float density, int max) {
        floatability = density;
        maxSpeed = max;
        System.out.println("type 5 duck");
        System.out.print("floatability = " + floatability + "\t xSpeed = " + maxSpeed + "\n");
    }

    /*
     * setter与getter
     * */
    public void setSize(int newSize) {
        size = newSize;
    }
    public int getSize() {
        return size;
    }
}
