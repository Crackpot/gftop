class XCopy {
    public static void main(String[] args) {

        int orig = 42;

        XCopy x = new XCopy();

        int y = x.go(orig);

        System.out.println(orig + " " + y);
    }
    int go(int arg) {// arg来自类的实例变量orig，初始值为42
        arg = arg * 2;
        return arg;
    }
}
