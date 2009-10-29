public class Overloads {

    // 实例变量
    String uniqueID;

    /*
     * 不同参数，不同返回值的同名函数
     * 1.返回类型可以不同
     * 2.不能只改变返回类型
     * 3.可以更改存取权限
     * */
    public int addNums(int a, int b) {
        return a + b;
    }
    public double addNums(double a, double b) {
        return a + b;
    }

    public void setUniqueID(String theID) {
        this.uniqueID = theID;
    }
    public void setUniqueID(int ssNumber) {
        String numString = "" + ssNumber;
        setUniqueID(numString);
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Overloads OverloadsInstance = new Overloads();
        OverloadsInstance.setUniqueID("910530526");
        System.out.println("The uniqueID is " + OverloadsInstance.uniqueID);
        OverloadsInstance.setUniqueID(68217555);
        System.out.println("The uniqueID is " + OverloadsInstance.uniqueID);
        System.out.println("The sum of the two numbers is " + OverloadsInstance.addNums(4, 5));
        System.out.println("The sum of the two numbers is " + OverloadsInstance.addNums(4.32, 5.93));
    }
}
