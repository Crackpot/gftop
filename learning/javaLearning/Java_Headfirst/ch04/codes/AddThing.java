class AddThing {
    int a;
    int b = 12;

    public int add() {
        // 局部变量是声明在方法中的
        int total = a + b;
        return total;
    }
}
