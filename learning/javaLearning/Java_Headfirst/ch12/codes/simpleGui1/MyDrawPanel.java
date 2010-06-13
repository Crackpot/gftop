import java.awt.*;
import javax.swing.*;

class MyDrawPanel extends JPanel {// 创建JPanel的子类
    public void paintComponent(Graphics g) {// 这是非常重要的方法，决不能自己调用，要由系统来调用。
        /*
         * 可以把g想象成绘图装置，告诉它要用什么颜色画出什么形状。
         * */
        g.setColor(Color.orange);
        g.fillRect(20, 50, 100, 100);
        /*
         * 显示JPEG
         * */
        Image image = new ImageIcon("myPicture.jpg").getImage();
        g.drawImage(image, 3, 4, this);// 这个坐标代表图案左上角的位置离panel的左方边缘3个像素，离顶端向下4个像素。
    }
}
