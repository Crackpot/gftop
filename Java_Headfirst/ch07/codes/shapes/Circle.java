public class Circle extends Shape {

    private Circle() { //没有参数的构造器
    }

    private Circle(String name) {// 一个参数的构造器
        this.setName(name); //调用父类方法
    }

    static public void main(String[] args) {
        Circle CircleInstance = new Circle("圆形");
        CircleInstance.rotate();
        CircleInstance.playSound();
    }
}
