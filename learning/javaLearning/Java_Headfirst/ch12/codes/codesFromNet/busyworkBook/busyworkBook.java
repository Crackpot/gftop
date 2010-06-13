/****************************************************************/
/* @(#)busyworkBook.java 1.0.0 2004-06-04 */
/* */
/* Email: pqdb123@yahoo.com.cn */
/* */
/* Copyright (c) 2004-2006 by ZhangYunFeng All Rights Reserved. */
/****************************************************************/
//导入awt包，event包
import java.awt.*;
import java.awt.event.*;
//定义busyworkBook类，继承类WindowAdapter，接口ActionListener
public class busyworkBook extends WindowAdapter implements ActionListener{
    Frame f=new Frame("JAVA作业本1.0.0 Writer:ZhangYunFeng"); //实例化框架 f
    TextArea a=new TextArea(); //实例化文本输入区
    //定义主方法
    public static void main(String args[]){
        busyworkBook book=new busyworkBook();
        book.go();
    }
    //定义go方法
    public void go(){
        f.addWindowListener(this); //注册监听器
        f.setBounds(100,100,600,480); //设置位置和大小
        f.setBackground(new Color(0x9f,0x8f,0x7f)); //设置背景色
        f.setVisible(true); //设置为可见
        f.add(a,"Center"); //把文本输入区添加到框架的Center位置
        MenuBar mb=new MenuBar(); //实例化MenuBar类的mb
        f.setMenuBar(mb); //加入框架，用setMenuBar
        Menu m1=new Menu("文件"); //实例化Menu类的m1，m2，m3，m4，m5
        Menu m2=new Menu("编辑");
        Menu m3=new Menu("格式");
        Menu m4=new Menu("窗口");
        Menu m5=new Menu("帮助");
        mb.add(m1); //加到mb
        mb.add(m2);
        mb.add(m3);
        mb.add(m4);
        mb.setHelpMenu(m5);
        MenuItem m101=new MenuItem("新建"); //实例化MenuItem类的m101，m102，m103，m104，m105
        MenuItem m102=new MenuItem("打开");
        MenuItem m103=new MenuItem("保存");
        MenuItem m104=new MenuItem("另存为");
        MenuItem m105=new MenuItem("退出");
        m105.addActionListener(new ActionListener(){ //注册监听器 匿名类开始
            public void actionPerformed(ActionEvent e){
                System.exit(1);
            }
        }); //匿名类结束
        m103.addActionListener(this);
        m1.add(m101); //加到m1上
        m1.add(m102);
        m1.add(m103);
        m1.add(m104);
        m1.addSeparator();
        m1.add(m105);
        MenuItem m201=new MenuItem("剪切"); //实例化MenuItem类的m201，m202，m203，m204，m205
        MenuItem m202=new MenuItem("复制");
        MenuItem m203=new MenuItem("粘贴");
        MenuItem m204=new MenuItem("全选");
        MenuItem m205=new MenuItem("查找");
        m2.add(m201); //加到m2上
        m2.add(m202);
        m2.add(m203);
        m2.addSeparator();
        m2.add(m204);
        m2.add(m205);
        MenuItem m301=new MenuItem("字体"); //实例化MenuItem类的m301，m302
        MenuItem m302=new MenuItem("段落");
        m3.add(m301); //加到m3上
        m3.add(m302);
        MenuItem m401=new MenuItem("状态栏"); //实例化MenuItem类的m401
        m4.add(m401); //加到m4上
        MenuItem m501=new MenuItem("帮助主题"); //实例化MenuItem类的m501，m502
        MenuItem m502=new MenuItem("关于作业本");
        m502.addActionListener(new ActionListener(){ //注册监听器
            public void actionPerformed(ActionEvent e){
                pin();
            }
        });
        m5.add(m501); //加到m5上
        m5.add(m502);
    }
    //重定windowClosing方法
    public void windowClosing(WindowEvent e){
        System.exit(1);
    }
    //重写actionPerformed方法
    public void actionPerformed(ActionEvent e){
        FileDialog d=new FileDialog(f,"FileDialog"); //f在内部引用要定义为final类型
        d.setVisible(true);
        String filename=d.getFile();
    }
    public void pin(){
        final Dialog dl=new Dialog(f,"关于JAVA作业本1.0.0");
        dl.addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent e){
                dl.setVisible(false);
            }
        });
        dl.setBounds(200,200,400,100);
        dl.setBackground(Color.yellow);
        Label l1=new Label("JAVA作业本1.0.0版，作者:ZHANG YUN FENG, 2004-06-05",Label.CENTER);
        dl.setLayout(new BorderLayout());
        dl.add(l1,"Center");
        dl.setVisible(true);
    }
}
