import javax.swing.*;// 别忘了import这个包

public class SimpleGui1 {
    public static void main(String[] args) {
        // 创建GUI的步骤：
        // 步骤1 创建frame。
        JFrame frame = new JFrame();
        // 步骤2 创建widget。
        JButton button = new JButton("click me");

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);// 这一行程序会在window关闭时把程序结束掉。
        // 步骤3 把widget加到frame上。
        frame.getContentPane().add(button);// 把button加到frame的panel上
        // 步骤4 显式出来。
        frame.setSize(300,300);// 设定frame的大小
        frame.setVisible(true);// 最后把frame显式出来
    }
}
