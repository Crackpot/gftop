class Foo {
    public int go() {
        // 局部变量在使用前必须初始化，局部变量没有初始值
        int x = (int)(Math.random() * 10);// 不初始化变量x时无法编译
        int z = x + 3;
        return z;
    }
}
