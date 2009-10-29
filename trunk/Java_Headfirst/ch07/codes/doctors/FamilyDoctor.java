public class FamilyDoctor extends Doctor {

    private FamilyDoctor() {
    }

    private FamilyDoctor(String name) {
        this.setName(name);
    }

    /* 自身的方法 */
    private void giveAdvice() {
        System.out.println(this.name + "提出诊断 (子类自身的方法)"); //在父类中name属性的类型上选用protected
    }

    public static void main(String[] args) {
        FamilyDoctor FamilyDoctorInstance = new FamilyDoctor("家庭医生");
        FamilyDoctorInstance.treatPatient();
        FamilyDoctorInstance.giveAdvice();
    }
}
