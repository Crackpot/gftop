public class Agent extends Robot {
    /*
     * 构造器
     * */
    protected Agent() {
    }
    protected Agent(String name) {
        super(name);//调用父类的构造函数
        System.out.println(this.name + "是机器人");
        //this.setName(name);
    }
    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Agent AgentInstance = new Agent("机器人");
    }
}
