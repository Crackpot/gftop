import javax.swing.*;
import java.awt.event.*;// import进ActionListener和ActionEvent所在的包

public class SimpleGui1B implements ActionListener {// 实现此接口。这表示SimpleGui1B是个ActionListener(事件只会通知有实现ActionListener的类)
    JButton button;

    public static void main(String[] args) {
        SimpleGui1B gui = new SimpleGui1B();
        gui.go();
    }

    public void go() {
        // 创建GUI的步骤
        // 步骤1 创建frame。
        JFrame frame = new JFrame();
        // 步骤2 创建widget。
        button = new JButton("click me!");

        button.addActionListener(this);// 向按钮注册

        // 步骤2 把widget添加到frame上。
        frame.getContentPane().add(button);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//这一行程序会在window关闭时把程序结束掉。
        frame.setSize(300,300);

        // 步骤4 显式出来。
        frame.setVisible(true);
    }
    public void actionPerformed(ActionEvent event) {// 实现interface上的方法，这才是真正处理事件的方法！ 按钮会以ActionEvent对象作为参数来调用此方法。
        button.setText("I've been clicked!");
    }
}
/*
 * 监听和事件源如何沟通
 *     监听
 *        如果类想要知道按钮的ActionEvent，你就得实现ActionListener这个接口。按钮需要知道你关注的部分，因此要通过调用addActionListener(this)并传入ActionListener的引用来向按钮注册。按钮会在该事件发生时调用该接口上的方法。而作为一个ActionListener，编译器会确保你实现此接口的actionPerformed()。
 *     事件源
 *        按钮是ActionEvent的来源，因此它必须要知道有哪些对象是需要事件通知的。此按钮有个addActionListener()方法可以提供对事件有兴趣的对象(listener)一种表达此兴趣的方法。当按钮的addActionListener()方法被调用时(因为某个listener的调用)，它的参数会被按钮存到清单中。当用户按下按钮时，按钮会通过调用清单上每个监听的actionPerformed()来启动事件。
 * */
/*
 * 取得按钮的ActionEvent
 *      1 实现ActionListener这个接口。
 *      2 向按钮注册(告诉它你要监听的事件)。
 *      3 定义事件处理的方法(实现接口上的方法)。
 * */
