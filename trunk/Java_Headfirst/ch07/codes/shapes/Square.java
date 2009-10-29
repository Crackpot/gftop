class Square extends Shape {

    private Square() { // 没有参数的构造器
    }

    private Square(String name) { // 一个参数的构造器
        this.setName(name);
    }

    public static void main(String[] args) {
        Square SquareInstance = new Square("长方形");
        SquareInstance.rotate();
        SquareInstance.playSound();
    }
}
