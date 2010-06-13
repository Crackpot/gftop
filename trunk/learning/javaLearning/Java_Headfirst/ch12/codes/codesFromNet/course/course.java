import java.awt.*;
import java.awt.List;
import java.awt.event.*;
import java.util.*;
class p1 extends Panel
{
    Label l1;
    Font f=new Font("宋体",Font.BOLD,20);
    p1()
    {
        setLayout(new GridLayout(1,1));
        l1=new Label("网上选课记录系统",Label.CENTER);
        l1.setFont(f);
        add(l1);
    }
}
class p2 extends Panel
{
    Label l1,l2;
    TextField t1,t2;
    p2()
    {
        setLayout(new GridLayout(1,4));
        l1=new Label("姓名",Label.CENTER);
        l2=new Label("学号",Label.CENTER);
        t1=new TextField(10);
        t2=new TextField(10);
        add(l1);
        add(t1);
        add(l2);
        add(t2);
    }
}
class p3 extends Panel
{
    Label l1,l2;
    TextField t1,t2;
    p3()
    {
        setLayout(new GridLayout(1,4));
        l1=new Label("专业",Label.CENTER);
        l2=new Label("所属院(系)",Label.CENTER);
        t1=new TextField(10);
        t2=new TextField(10);
        add(l1);
        add(t1);
        add(l2);
        add(t2);
    }
}
class p4 extends Panel
{
    Label l1;
    Button btn1;
    Button btn2;
    Button btn3;
    Font f=new Font("宋体",Font.BOLD,20);
    p4()
    {
        setLayout(new GridLayout(1,4));
        l1=new Label("请选择您要选修的课程并确认",Label.CENTER);
        btn1=new Button("查询");
        btn2=new Button("确认");
        btn3=new Button("退出系统");
        add(l1);
        add(btn1);
        add(btn2);
        add(btn3);
    }
}
class p5 extends Panel
{
    List list ;
    p5()
    {
        setLayout(new GridLayout(1,1));
        list=new List(8,true);
        list.add("大学英语");
        list.add("计算机图形学");
        list.add("JAVA语言");
        list.add("高等数学");
        list.add("数据结构");
        list.add("单片机");
        list.add("网络应用与开发");
        list.add("概率论与数理统计");
        list.add("管理学概论");
        list.add("数据库概论");
        list.add("英语听力");
        list.add("VC++");
        list.add("商务英语");
        list.add("会计学");
        list.add("经济学");
        list.add("计算机网络");
        add(list);
    }
}
class p6 extends Panel
{
    TextArea ta;
    p6()
    {
        setLayout(new GridLayout(1,1));
        ta=new TextArea(8,30);
        add(ta);
    }
}
class p8 extends Panel
{
    Label l1,l2,l3;
    Label l4,l5,l6,l7,l9;
    Panel p11,p22,p33,p44,p55;
    TextField t1,t2;
    Button btn;
    p8()
    {
        p11=new Panel();
        p22=new Panel();
        p33=new Panel();
        p44=new Panel();
        p55=new Panel();
        p11.setLayout(new GridLayout(1,1));
        p22.setLayout(new GridLayout(1,1));
        p33.setLayout(new GridLayout(1,4));
        p44.setLayout(new GridLayout(1,4));
        p55.setLayout(new GridLayout(1,1));
        l4=new Label("");
        l5=new Label("");
        l6=new Label("");
        l7=new Label("");
        l9=new Label("");
        l1=new Label("欢迎来到网上选课系统",Label.CENTER);
        Font f=new Font("宋体",Font.BOLD,30);
        l1.setFont(f);
        l2=new Label("请输入管理员帐号",Label.CENTER);
        l3=new Label("请输入管理员密码",Label.CENTER);
        setBackground(Color.lightGray);
        btn=new Button("确定");
        t1=new TextField(20);
        t2=new TextField(15);
        t2.setEchoChar('*');
        l1.setForeground(Color.magenta);
        t1.setBackground(Color.cyan);
        t2.setBackground(Color.cyan);
        t1.setForeground(Color.red);
        t2.setForeground(Color.red);
        l2.setForeground(Color.blue);
        l3.setForeground(Color.blue);
        p11.add(l1);
        p22.add(l4);
        p33.add(l5);
        p33.add(l2);
        p33.add(t1);
        p33.add(l6);
        p44.add(l7);
        p44.add(l3);
        p44.add(t2);
        p44.add(btn);
        p55.add(l9);
        setLayout(new GridLayout(5,1));
        add(p11);
        add(p22);
        add(p33);
        add(p44);
        add(p55);
    }
}
class p9 extends Panel
{
    p1 pn1=new p1();
    p2 pn2=new p2();
    p3 pn3=new p3();
    p4 pn4=new p4();
    p5 pn5=new p5();
    p6 pn6=new p6();
    p9()
    {
        setLayout(new GridLayout(6,1));
        add(pn1);
        add(pn2);
        add(pn3);
        add(pn4);
        add(pn5);
        add(pn6);
    }
}
class user
{
    String username;
    String sd;
    String major;
    String institute;
    String course;
    user(String x1,String x2,String x3,String x4,String x5)
    {
        username=x1;
        sd=x2;
        major=x3;
        institute=x4;
        course=x5;
    }
}
public class course
{
    public static void main(String args[])
    {
        new m();
    }
}
class m extends Frame implements ActionListener,ItemListener
{
    StringBuffer ss=new StringBuffer("您好!您选修的课程有:");
    Vector xiang=new Vector();
    p9 pn9;
    p8 pn8;
    CardLayout cc=new CardLayout();
    Button btn1;
    Dialog d1;
    m()
    {
        super("网上选课");
        pn8=new p8();
        pn9=new p9();
        setLayout(cc);
        add("one",pn8);
        add("two",pn9);
        btn1=new Button("确定");
        pn9.pn1.l1.setBackground(Color.pink);
        pn9.pn1.l1.setForeground(Color.blue);
        pn9.pn2.l1.setBackground(Color.gray);
        pn9.pn2.l1.setForeground(Color.orange);
        pn9.pn2.l2.setBackground(Color.gray);
        pn9.pn2.l2.setForeground(Color.orange);
        pn9.pn3.l1.setBackground(Color.gray);
        pn9.pn3.l1.setForeground(Color.orange);
        pn9.pn3.l2.setBackground(Color.gray);
        pn9.pn3.l2.setForeground(Color.orange);
        pn9.pn2.t1.setForeground(Color.red);
        pn9.pn2.t1.setBackground(Color.cyan);
        pn9.pn2.t2.setForeground(Color.red);
        pn9.pn2.t2.setBackground(Color.cyan);
        pn9.pn3.t1.setForeground(Color.red);
        pn9.pn3.t1.setBackground(Color.cyan);
        pn9.pn3.t2.setForeground(Color.red);
        pn9.pn3.t2.setBackground(Color.cyan);
        pn9.pn5.list.setBackground(Color.pink);
        pn9.pn5.list.setForeground(Color.blue);
        pn9.pn6.ta.setBackground(Color.blue);
        pn9.pn6.ta.setForeground(Color.white);
        pn9.pn4.btn1.addActionListener(this);
        pn9.pn4.btn2.addActionListener(this);
        pn9.pn4.btn3.addActionListener(this);
        pn9.pn5.list.addActionListener(this);
        (pn9.pn5.list).addItemListener(this);
        pn8.btn.addActionListener(this);
        btn1.addActionListener(this);
        setSize(650,400);
        show();
    }
    public void actionPerformed(ActionEvent e)
    {
        xiang.addElement(new user("马先生","23597483","计算机","计算机系","单片机，数学"));
        xiang.addElement(new user("杨先生","7899452","计算机","计算机系","单片机，数学"));
        xiang.addElement(new user("董先生","7899452","计算机","计算机系","单片机，数学"));
        xiang.addElement(new user("何先生","7899453","计算机","计算机系","单片机，数学"));
        if(e.getSource()==pn8.btn)
        {
            String ss="123";
            if(ss.compareTo(pn8.t1.getText())==0&&ss.compareTo(pn8.t2.getText())==0)
                cc.show(this,"two");
            else
            {
                d1=new Dialog(this,"警告",true);
                Panel p1=new Panel();
                p1.add(new Label("您无权进本系统!"));
                d1.add("Center",p1);
                Panel p2=new Panel();
                p2.add(btn1);
                d1.add("South",p2);
                d1.setSize(200,100);
                d1.show();
            }
        }
        if(e.getSource()==btn1)
        {
            d1.dispose();
        }
        if(e.getSource()==pn9.pn4.btn3)
        {
            dispose();
            System.exit(0);
        }
        if(e.getSource()==pn9.pn4.btn2)
        {
            pn9.pn6.ta.setText("");
            ss.append(" 您的姓名是:"+pn9.pn2.t1.getText()+" "+"您的学号是:"+pn9.pn2.t2.getText()+" ");
            ss.append("您的专业是:"+pn9.pn3.t1.getText()+" "+"您所在院(系)是:"+pn9.pn3.t2.getText()+" ");
            ss.append("您的所有信息将被保存!");
            pn9.pn6.ta.setText(ss.toString());
            user s1=new user(pn9.pn2.t1.getText(),pn9.pn2.t2.getText(),pn9.pn3.t1.getText(),pn9.pn3.t2.getText(),ss.toString());
            int i;
            for(i=0;i<xiang.size();i++)
            {
                user s=(user)xiang.elementAt(i);
                if(s.sd.compareTo(s1.sd)==0)
                {
                    s.username=s1.username;
                    s.sd=s1.sd;
                    s.major=s1.major;
                    s.institute=s1.institute;
                    s.course=s1.course;
                    xiang.setElementAt(new user(s.username,s.sd,s.major,s.institute,s.course),i);
                    break;
                }
            }
            if(i==xiang.size())
                xiang.addElement(new user(pn9.pn2.t1.getText(),pn9.pn2.t2.getText(),pn9.pn3.t1.getText(),pn9.pn3.t2.getText(),ss.toString()));
        }
        if(e.getSource()==pn9.pn4.btn1)
        {
            pn9.pn6.ta.setText("");
            if(pn9.pn2.t2.getText()=="")
            {
                d1=new Dialog(this,"注意",true);
                Panel p1=new Panel();
                p1.add(new Label("按学号进行查询!请输入学号!再按此键!"));
                d1.add("Center",p1);
                Panel p2=new Panel();
                p2.add(btn1);
                d1.add("South",p2);
                d1.setSize(250,100);
                d1.show();
            }
            int i;
            for(i=0;i<xiang.size();i++)
            {
                user s=(user)xiang.elementAt(i);
                if(s.sd.compareTo(pn9.pn2.t2.getText())==0)
                {
                    pn9.pn2.t1.setText(""+s.username);
                    pn9.pn3.t1.setText(""+s.major);
                    pn9.pn3.t2.setText(""+s.institute);
                    pn9.pn6.ta.setText("您选修的课程有:"+s.course);
                    break;
                }
            }
            if(i==xiang.size())
            {
                d1=new Dialog(this,"警告",true);
                Panel p1=new Panel();
                p1.add(new Label("用户不存在!请重新输入!"));
                d1.add("Center",p1);
                Panel p2=new Panel();
                p2.add(btn1);
                d1.add("South",p2);
                d1.setSize(200,100);
                d1.show();
            }
        }
    }
    public void itemStateChanged(ItemEvent e)
    {
        List temp;
        String sList[];
        String mgr=new String("");
        if(e.getItemSelectable()instanceof List)
        {
            temp=(List)(e.getItemSelectable());
            sList=temp.getSelectedItems();
            for(int i=0;i<sList.length;i++)
                mgr=mgr+sList[i]+" ";
            ss.append(mgr);
        }
    }
}

