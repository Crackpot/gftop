import java.awt.*;
import java.awt.event.*;
import java.util.*;

class p1 extends Panel {
    Label l1;
    Font f=new Font("宋体",Font.BOLD,20);
    p1() {
        setLayout(new GridLayout(1,1));
        l1=new Label("用户电话号码管理",Label.CENTER);
        l1.setFont(f);
        add(l1);
    }
}

class p2 extends Panel {
    Label l1,l2;
    TextField t1,t2;
    p2() {
        setLayout(new GridLayout(1,4));
        l1=new Label("姓名",Label.CENTER);
        l2=new Label("身份证号",Label.CENTER);
        t1=new TextField(10);
        t2=new TextField(10);
        add(l1);
        add(t1);
        add(l2);
        add(t2);
    }
}

class p3 extends Panel {
    Label l1,l2;
    TextField t1,t2;
    p3() {
        setLayout(new GridLayout(1,4));
        l1=new Label("家庭住址",Label.CENTER);
        l2=new Label("电话号码",Label.CENTER);
        t1=new TextField(10);
        t2=new TextField(10);
        add(l1);
        add(t1);
        add(l2);
        add(t2);
    }
}

class p4 extends Panel {
    Label l1,l2;
    TextField t1,t2;
    Button btn1;
    p4() {
        setLayout(new GridLayout(1,5));
        l1=new Label("话费余额",Label.CENTER);
        l2=new Label("预交话费",Label.CENTER);
        t1=new TextField(15);
        t2=new TextField(15);
        btn1=new Button("确认");
        add(l1);
        add(t1);
        add(l2);
        add(t2);
        add(btn1);
    }
}

class p5 extends Panel {
    Label l1;
    TextField t1;
    p5() {
        setLayout(new GridLayout(1,2));
        l1=new Label("预交时话费总额",Label.CENTER);
        t1=new TextField(20);
        add(l1);
        add(t1);
    }
}

class p6 extends Panel {
    Button btn1,btn2;
    p6() {
        setLayout(new GridLayout(1,2));
        btn1=new Button("按用户姓名查询");
        btn2=new Button("按电话号码查询");
        add(btn1);
        add(btn2);
    }
}

class p7 extends Panel {
    Button btn1,btn2,btn3,btn4,btn5;
    p7() {
        setLayout(new GridLayout(1,5));
        btn1=new Button("修改");
        btn2=new Button("添加");
        btn3=new Button("删除");
        btn4=new Button("清空");
        btn5=new Button("退出系统");
        add(btn1);
        add(btn2);
        add(btn3);
        add(btn4);
        add(btn5);
    }
}

class user {
    String username;
    String id;
    String address;
    String phonenumber;
    double phonefee;
    user(String x1,String x2,String x3,String x4,double x5) {
        username=x1;
        id=x2;
        address=x3;
        phonenumber=x4;
        phonefee=x5;
    }
}

class p8 extends Panel {
    Label l1,l2,l3;
    Label l4,l5,l6,l7,l9;
    Panel p11,p22,p33,p44,p55;
    TextField t1,t2;
    Button btn;
    p8() {
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
        l1=new Label("欢迎来到电话管理系统",Label.CENTER);
        Font f=new Font("宋体",Font.BOLD,30);
        l1.setFont(f);
        l2=new Label("请输入管理员帐号",Label.CENTER);
        l3=new Label("请输入管理员密码",Label.CENTER);
        setBackground(Color.pink);
        btn=new Button("确定");
        t1=new TextField(20);
        t2=new TextField(15);
        t2.setEchoChar('*');
        l1.setForeground(Color.red);
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

class p9 extends Panel {
    p1 pn1=new p1();
    p2 pn2=new p2();
    p3 pn3=new p3();
    p4 pn4=new p4();
    p5 pn5=new p5();
    p6 pn6=new p6();
    p7 pn7=new p7();
    p9() {
        setLayout(new GridLayout(7,1));
        add(pn1);
        add(pn2);
        add(pn3);
        add(pn4);
        add(pn5);
        add(pn6);
        add(pn7);
    }
}

public class TelphoneAdmin {
    public static void main(String args[])
    {
        new zz();
    }
}

class zz extends Frame implements ActionListener {
    Vector v=new Vector();
    Button btn1;
    p9 pn9;
    p8 pn8;
    Dialog d1;
    CardLayout cc=new CardLayout();
    zz() {
        super("用户电话档案管理");
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
        pn9.pn4.t1.setForeground(Color.red);
        pn9.pn4.t1.setBackground(Color.cyan);
        pn9.pn4.t2.setForeground(Color.red);
        pn9.pn4.t2.setBackground(Color.cyan);
        pn9.pn4.l1.setBackground(Color.gray);
        pn9.pn4.l1.setForeground(Color.orange);
        pn9.pn4.l2.setBackground(Color.gray);
        pn9.pn4.l2.setForeground(Color.orange);
        pn9.pn5.l1.setBackground(Color.pink);
        pn9.pn5.l1.setForeground(Color.blue);
        pn9.pn5.t1.setBackground(Color.cyan);
        pn9.pn5.t1.setForeground(Color.red);
        pn9.pn4.btn1.addActionListener(this);
        pn9.pn6.btn1.addActionListener(this);
        pn9.pn6.btn2.addActionListener(this);
        pn9.pn7.btn1.addActionListener(this);
        pn9.pn7.btn2.addActionListener(this);
        pn9.pn7.btn3.addActionListener(this);
        pn9.pn7.btn4.addActionListener(this);
        pn9.pn7.btn5.addActionListener(this);
        pn8.btn.addActionListener(this);
        btn1.addActionListener(this);
        setSize(600,300);
        show();
    }

    public void actionPerformed(ActionEvent e) {
        v.addElement(new user("何先生","370723800121597","中国","5866681",100.0));
        v.addElement(new user("马先生","370723800121591","中国","5866680",100.0));
        v.addElement(new user("徐先生","370723800121592","中国","5866689",100.0));
        v.addElement(new user("李先生","370723800121593","中国","5866687",100.0));
        v.addElement(new user("董先生","370723800121594","中国","5866688",100.0));
        v.addElement(new user("张先生","370723800121595","中国","5866686",100.0));
        v.addElement(new user("闻先生","370723800121596","中国","5866685",100.0));
        v.addElement(new user("张先生","370723800121598","中国","5866684",100.0));
        v.addElement(new user("杨先生","370723800121599","中国","5866683",100.0));
        v.addElement(new user("孔先生","370723800121590","中国","5866682",100.0));
        if(e.getSource()==pn8.btn) {
            String ss="123";//用户名密码
            if(ss.compareTo(pn8.t1.getText())==0&&ss.compareTo(pn8.t2.getText())==0)
                cc.show(this,"two");
            else {
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
        if(e.getSource()==pn9.pn4.btn1)
        {
            double x1,x2,x3;
            x1=Double.valueOf(pn9.pn4.t1.getText()).doubleValue();
            x2=Double.valueOf(pn9.pn4.t2.getText()).doubleValue();
            x3=x1+x2;
            pn9.pn5.t1.setText(""+x3);
            int i;
            for(i=0;i<v.size();i++) {
                user s=(user)v.elementAt(i);
                if(s.username.compareTo(pn9.pn2.t1.getText())==0) {
                    s.phonefee=x3;
                    v.setElementAt(s,i);
                    break;
                }
            }
        }
        if(e.getSource()==pn9.pn6.btn1) {
            int i;
            for(i=0;i<v.size();i++) {
                user s=(user)v.elementAt(i);
                if(s.username.compareTo(pn9.pn2.t1.getText())==0) {
                    pn9.pn2.t2.setText(""+s.id);
                    pn9.pn3.t1.setText(""+s.address);
                    pn9.pn3.t2.setText(""+s.phonenumber);
                    pn9.pn4.t1.setText(""+s.phonefee);
                    break;
                }
            }
            if(i==v.size()) {
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
        if(e.getSource()==pn9.pn6.btn2) {
            int i;
            for(i=0;i<v.size();i++) {
                user s=(user)v.elementAt(i);
                if(s.phonenumber.compareTo(pn9.pn3.t2.getText())==0) {
                    pn9.pn2.t1.setText(""+s.username);
                    pn9.pn2.t2.setText(""+s.id);
                    pn9.pn3.t1.setText(""+s.address);
                    pn9.pn4.t1.setText(""+s.phonefee);
                    break;
                }
            }
            if(i==v.size()) {
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
        if(e.getSource()==pn9.pn7.btn5) {
            dispose();
            System.exit(0);
        }
        if(e.getSource()==btn1)
        {
            d1.dispose();
        }
        if(e.getSource()==pn9.pn7.btn1)
        {
            int i;String m1,m2,m3,m4; double m5;
            for(i=0;i<v.size();i++)
            {
                user s=(user)v.elementAt(i);
                if(s.id.compareTo(pn9.pn2.t2.getText())==0)
                {
                    m1=pn9.pn2.t1.getText();
                    m2=pn9.pn2.t2.getText();
                    m3=pn9.pn3.t1.getText();
                    m4=pn9.pn3.t2.getText();
                    m5=Double.valueOf(pn9.pn4.t1.getText()).doubleValue();
                    s.username=m1;
                    s.id=m2;
                    s.address=m3;
                    s.phonenumber=m4;
                    s.phonefee=m5;
                    v.setElementAt(s,i);
                    d1=new Dialog(this,"恭喜",true);
                    Panel p1=new Panel();
                    p1.add(new Label("用户已修改成功!"));
                    d1.add("Center",p1);
                    Panel p2=new Panel();
                    p2.add(btn1);
                    d1.add("South",p2);
                    d1.setSize(200,100);
                    d1.show();
                    break;
                }
            }
            if(i==v.size()) {
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
        if(e.getSource()==pn9.pn7.btn2) {
            String m1,m2,m3,m4; double m5;
            m1=pn9.pn2.t1.getText();
            m2=pn9.pn2.t2.getText();
            m3=pn9.pn3.t1.getText();
            m4=pn9.pn3.t2.getText();
            m5=Double.valueOf(pn9.pn4.t1.getText()).doubleValue();
            v.addElement(new user(m1,m2,m3,m4,m5));
            d1=new Dialog(this,"恭喜",true);
            Panel p1=new Panel();
            p1.add(new Label("用户添加成功!"));
            d1.add("Center",p1);
            Panel p2=new Panel();
            p2.add(btn1);
            d1.add("South",p2);
            d1.setSize(200,100);
            d1.show();
        }
        if(e.getSource()==pn9.pn7.btn3) {
            int i;
            for(i=0;i<v.size();i++) {
                user s=(user)v.elementAt(i);
                if(s.phonenumber.compareTo(pn9.pn3.t2.getText())==0)
                    v.removeElement(s);
                d1=new Dialog(this,"恭喜",true);
                Panel p1=new Panel();
                p1.add(new Label("用户成功移除!"));
                d1.add("Center",p1);
                Panel p2=new Panel();
                p2.add(btn1);
                d1.add("South",p2);
                d1.setSize(200,100);
                d1.show();
                break;
            }
        }
        if(e.getSource()==pn9.pn7.btn4) {
            pn9.pn2.t1.setText("");
            pn9.pn2.t2.setText("");
            pn9.pn3.t1.setText("");
            pn9.pn3.t2.setText("");
            pn9.pn4.t1.setText("");
            pn9.pn4.t2.setText("");
            pn9.pn5.t1.setText("");
        }
    }
}
