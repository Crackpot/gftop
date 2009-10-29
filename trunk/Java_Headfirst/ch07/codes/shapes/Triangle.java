public class Triangle extends Shape {

    private Triangle() { //无参数构造器
    }

    private Triangle(String name) { //单参数构造器
        this.setName(name); //调用父类方法
    }

    public static void main(String[] args) {
        Triangle TriangleInstance = new Triangle("三角形");
        TriangleInstance.rotate();
        TriangleInstance.playSound();
    }
}
