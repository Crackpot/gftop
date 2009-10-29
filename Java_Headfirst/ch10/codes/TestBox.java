public class TestBox {
    int j;//0
    Integer i;//null
    public static void main(String[] args) {
        TestBox t = new TestBox();
        t.go();
    }
    public void go() {
        //j = Integer.parseInt(i);
        //j = i;//出现异常，原因是值为null的i无法给j赋值
        i = j;//颠倒就可以了
        System.out.println(j);
        System.out.println(i);
    }
}
