public class GuessGame {
    // 用3个实例变量分别表示3个Player对象
    Player p1;
    Player p2;
    Player p3;

    public void startGame() {
        // 创建出Player对象
        p1 = new Player();
        p2 = new Player();
        p3 = new Player();

        // 声明3个变量保存是否猜中
        int guessp1 = 0;
        int guessp2 = 0;
        int guessp3 = 0;

        //声明3个变量来保存猜测的数字
        boolean p1isRight = false;
        boolean p2isRight = false;
        boolean p3isRight = false;

        // 产生谜底数字
        int targetNumber = (int)(Math.random() * 10);
        System.out.println("I'm thinking of a number between 0 and 9...");

        while (true) {
            System.out.println("Number to guess is " + targetNumber);

            // 调用Player的guess()方法
            p1.guess();
            p2.guess();
            p3.guess();

            //取得每个Player所猜测的数字并将它列出
            guessp1 = p1.number;
            System.out.println("Player one guessed " + guessp1);
            guessp2 = p2.number;
            System.out.println("Player two guessed " + guessp2);
            guessp3 = p3.number;
            System.out.println("Player three guessed " + guessp3);

            // 检查是否猜中，若是猜中则去设定设定是否猜中的变量
            if (guessp1 == targetNumber) {
                p1isRight = true;
            }
            if (guessp2 == targetNumber) {
                p2isRight = true;
            }
            if (guessp3 == targetNumber) {
                p3isRight = true;
            }

            if (p1isRight || p2isRight || p3isRight) {
                System.out.println("We have a winner!");
                System.out.println("Player one got it right ? " + p1isRight);
                System.out.println("Player two got it right ? " + p2isRight);
                System.out.println("Player three got it right ? " + p3isRight);
                System.out.println("Game is over.");
                break;
            } else {
                // 都没猜到，所以要继续下去
                System.out.println("Player will have to try again");
            }
        }
    }
}
