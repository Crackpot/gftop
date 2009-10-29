public class HippoTestDrive {
    /*
     * 创建Hippo也代表创建Animal与Objec
     * 思考：小孩能够在父母之前出生么？
     * */
    public static void main(String[] args) {
        System.out.println("Starting...");
        //Hippo HippoInstance = new Hippo();
        Hippo HippoInstance = new Hippo("Buffy");
        System.out.println(HippoInstance.getClass() + "\t name = " + HippoInstance.getName());
    }
}
