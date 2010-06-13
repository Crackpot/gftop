import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class MyDrawPanel extends JPanel {
    public void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;// 将它的类型转换成Graphics2D
        /*
         * 渐进效果
         * */
        GradientPaint gradient = new GradientPaint(70, 70, Color.blue, 150, 150, Color.orange);// 开始坐标，开始颜色，结束坐标，结束颜色
        g2d.setPaint(gradient);//将虚拟的"笔刷"换成渐层
        g2d.fillOval(70, 70, 100, 100);// 用目前的笔刷设定来填满椭圆型的区域
    }
}
public class SimpleGui3C implements ActionListener {
    JFrame frame;
    public static void main(String[] args) {
        SimpleGui3C gui = new SimpleGui3C();
        gui.go();
    }
    public void go() {
        frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton button = new JButton("Change colors");
        button.addActionListener(this);

        MyDrawPanel drawPanel = new MyDrawPanel();

        frame.getContentPane().add(BorderLayout.SOUTH, button);
        frame.getContentPane().add(BorderLayout.CENTER, drawPanel);
        frame.setSize(300, 300);
        frame.setVisible(true);
    }
    public void actionPerformed(ActionEvent event) {
        frame.repaint();
    }
}
