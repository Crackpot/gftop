public class SimpleDotCom {
    int [] locationCells;
    int numOfHits = 0;

    public void setLocationCells(int[] locs) {
        locationCells = locs;
    }
    public String checkYourself(String StringGuess) {

        int guess = Integer.parseInt(StringGuess);// 把字符串转换成int

        String result = "miss";// 创建出保存返回结果的变量，以miss作为默认值

        for (int cell : locationCells) {// 以循环对每个格子重复执行

            if (guess == cell) {// 并将格子与猜测值

                // 命中
                result = "hit";
                numOfHits++;
                break;
            }
        }

        if (numOfHits == locationCells.length) {// 已经离开循环，但需要判断是否击沉
            result = "kill";
        }

        System.out.println(result);// 将结果显式出来

        return result;// 将结果返回给调用方
    }
}
/*
 * 此类中出现的重点：
 *     1 将string转换成int
 *          Integer.parseInt("3")
 *     2 for 循环
 *          for (int cell:locationCells) {}
 *          对locationCells中每个元素执行一次，每次循环都会将内容赋给cell变量
 * */
