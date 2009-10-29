public class PlayerTestDrive {
    public static void main(String[] args) {
        System.out.println(Player.playerCount);//创建实例之前为0

        Player one = new Player("Tiger Woods");
        System.out.println(Player.playerCount);

        Player two = new Player("Westlife");
        System.out.println(Player.playerCount);
    }
}
