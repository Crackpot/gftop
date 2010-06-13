public interface Pet {
    /*
     * 接口不是父类，不可以被继承，方法的修饰符不可用protected
     * 所有接口的方法都是抽象的。
     * */
    public abstract void beFriendly();
    public abstract void play();
}
