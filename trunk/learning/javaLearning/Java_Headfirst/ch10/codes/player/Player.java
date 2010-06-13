public class Player {
    /*
     * 实例变量
     * */
    static int playerCount = 0;//静态变量会在该类的任何静态方法执行之前就初始化。意在main之前就初始化了。
    private String name;

    /*
     * 构造函数
     * */
    public Player(String n) {
        name = n;
        System.out.println("演员姓名：" + this.getName());
        playerCount++;
    }
    /*
     * setter与getter
     * */
    public void setName(String name) {
        name = name;
    }
    public String getName() {
        return name;
    }
}
