public class Surgeon extends Doctor { //外科医生

    private Surgeon() {
    }

    private Surgeon(String name) {
        this.setName(name);
    }

    protected void treatPatient() { //覆盖父类具有的方法，用protected类型
        //进行手术
        System.out.println(this.name + "进行手术");
    }

    private void makeIncision() { //父类没有，子类自身具备的方法可以用private类型
        System.out.println(this.name + "截肢");
    }

    public static void main(String[] args) {
        Surgeon SurgeonInstance = new Surgeon("外科医生");
        SurgeonInstance.treatPatient();
        SurgeonInstance.makeIncision();
    }
}
