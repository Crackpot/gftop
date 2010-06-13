public class DotComTestDrive {

    public static void main(String[] args) {

        DotCom dot = new DotCom();// 初始化一个SimpleDotCom对象

        int[] locations = {2,3,4};// 创建带有dotCom位置的数组

        dot.setLocationCells(locations);// 调用dotCom的setter

        String userGuess = "2";// 假的猜测
        String result = dot.checkYourself(userGuess);// 调用方法并传入假的数据
        /*
         String testResult = "failed";
        if (result.equals("hit")) {
            testResult = "passed";// 测试应该要返回"hit"才算成功
        }
        System.out.println(testResult);
        */
    }
}
