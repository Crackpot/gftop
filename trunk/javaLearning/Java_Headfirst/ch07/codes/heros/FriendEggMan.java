public class FriendEggMan extends SuperHero {

    private FriendEggMan() {
    }

    private FriendEggMan(String name) {
        this.setName(name);
    }

    public static void main(String[] args) {
        FriendEggMan FriendEggManInstance = new FriendEggMan("FriendEggManInstance");
        FriendEggManInstance.useSpecialPower();
        FriendEggManInstance.putOnSuit();
    }
}
