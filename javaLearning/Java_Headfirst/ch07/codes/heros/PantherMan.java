public class PantherMan extends SuperHero {

    private PantherMan() {
    }

    private PantherMan(String name) {
        this.setName(name);
    }

    protected void useSpecialPower() {
        System.out.println("PantherMan类自身的useSpecialPower方法");
    }
    
    protected void putOnSuit() {
        System.out.println("PantherMan类自身的putOnSuit方法");
    }

    public static void main(String[] args) {
        PantherMan PantherManInstance = new PantherMan("PantherManInstance");
        PantherManInstance.useSpecialPower();
        PantherManInstance.putOnSuit();
    }
}
