public class SimpleDotComGame {
    public static void main(String[] args){

        int numOfGuesses = 0;// 记录玩家的猜测次数

        GameHelper helper = new GameHelper();// 我们会写出这个类来取得玩家的输入，现在先假装这是Java提供的。

        SimpleDotCom theDotCom = new SimpleDotCom();// 创建dotCom对象

        int randomNum = (int) (Math.random() * 5);// 用随机数产生第一格的位置，然后以此制作出数组
        int[] locations = {randomNum, randomNum + 1, randomNum + 2};// 连续的三个格子
        theDotCom.setLocationCells(locations);// 赋值位置

        boolean isAlive = true;// 创建出记录游戏是否继续进行的boolean变量，这回用在while循环中

        while(isAlive == true) {
            String guess = helper.getUserInput("enter a number");// 取得玩家输入的字符串
            String result = theDotCom.checkYourself(guess);// 检查玩家的猜测并将结果存储在String中
            numOfGuesses++;
            if (result.equals("kill")) {// 是否击沉，若击沉，则设定isAlive为false并输出猜测次数
                isAlive = false;
                System.out.println("You took " + numOfGuesses + " guesses");
            }
        }
    }
}
