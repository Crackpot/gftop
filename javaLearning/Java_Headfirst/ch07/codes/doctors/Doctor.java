public class Doctor { //父类

    protected String name; //在子类中有个方法也要用到name，故将类型改为protected
    boolean worksAtHospital;    /* 在医院工作 */
    
    protected void setName(String name) {
        this.name = name;
    }

    void treatPatient() {
        //执行检查
        System.out.println(this.name + "进行检查");
    }
}
