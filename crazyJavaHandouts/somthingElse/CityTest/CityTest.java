//可以通过拖动代表城市的小方块来观察效果，程序是用别的程序改过来的，有点乱
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import javax.swing.*;

public class CityTest implements Runnable{
  
   private int x,y;//
   private City[] cs;//城市数组
   private double min;//最短路径的值
   private int[] fin;//最短路径的城市ID数组
   private City start,end;//出发城市和目标城市
   private String str ="abcdefghijklmnopqrstuvwxyz";//不要改动
  
   public void run(){
       min=Double.MAX_VALUE;
       loop(new char[0],str.substring(0,cs.length).toCharArray(),cs.length);
   }
   //遍历所有可能组合
   public void loop(char[] t,char[] a,int l){
       if(l>1){
           for(int i=0; i<a.length; i++){
               char[] b = new char[t.length+1];
               System.arraycopy(t,0,b,0,t.length);
               b[t.length]=a[i];
               loop(b,a,l-1);
           }
       }
       else {
           for(int i=0; i<a.length; i++){
               process(t,a[i]);
           }
       }
       Thread.yield();
   }
   //求城市索引数组
   private final void process(char[] t, char c) {
       for(int i=0; i<t.length; i++){
           for(int j=i+1; j<t.length; j++){
               if(t[i]==t[j])
                   return;
           }
           if(t[i]==c)
               return;
       }
      
       int[] ti = new int[t.length+1];
       for(int i=0; i<t.length; i++)
           ti[i]=t[i]-'a';
       ti[t.length]=c-'a';
       dist(ti);
   }
   //求最短路径
   private void dist(int[] index) {
       double d = 0;
       City c = start;
       for(int i:index){
           d+=c.getDist(cs[i]);
           c=cs[i];
       }
       d+=c.getDist(end);
       if(min>d){
           min=d;
           fin=index;
       }
   }
   //程序入口
   public static void main(String[] args) {
       int pw=400,ph=400;
       int cts = 8;//城市个数（建议10个以下），我的电脑计算10城市时大概耗时10S，10个以上耗时很久(程序会停止响应,请重新设计程序)
      
       final City[] cs = new City[cts];
       for(int i=0; i<cts; i++){
           cs[i]=new City(i);
           cs[i].x=(int)(Math.random()*pw);
           cs[i].y=(int)(Math.random()*ph);
       }
      
       final City start = cs[0];
       final City dest = cs[cts-1];
       City[] loops = new City[cts-2];
       System.arraycopy(cs, 1, loops, 0, cts-2);
      
       final CityTest ct = new CityTest();
       ct.cs=loops;
       ct.start=start;
       ct.end=dest;
      
       //GUI部分
       final JPanel p = new JPanel(null);
       p.setPreferredSize(new Dimension(pw,ph));
       JFrame f = new JFrame();
       f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       f.setContentPane(p);
       f.pack();
       f.setLocationRelativeTo(null);
       f.setVisible(true);
      
       final JLabel[] ls = new JLabel[cts];
       for(int i=0; i<cts; i++){
           final int index = i;
           ls[i]=new JLabel(""+i);
           ls[i].setSize(20,20);
           ls[i].setHorizontalAlignment(JLabel.CENTER);
           ls[i].setBorder(BorderFactory.createLineBorder(Color.DARK_GRAY));
           f.add(ls[i]);
           ls[i].setLocation(cs[i].x-10,cs[i].y-10);
           ls[i].addMouseListener(new MouseListener(){
               public void mouseClicked(MouseEvent e) {}
               public void mouseEntered(MouseEvent e) {}
               public void mouseExited(MouseEvent e) {}
               public void mousePressed(MouseEvent e) {ct.x=e.getX();ct.y=e.getY();p.repaint();}
               public void mouseReleased(MouseEvent e) {
                   render(p,ct);
               }
           });
           ls[i].addMouseMotionListener(new MouseMotionListener(){
               public void mouseDragged(MouseEvent e) {
                   JLabel l = (JLabel)e.getSource();
                   l.setLocation(l.getX()+e.getX()-ct.x,l.getY()+e.getY()-ct.y);
                   cs[index].x=l.getX()+l.getWidth()/2;
                   cs[index].y=l.getY()+l.getHeight()/2;
               }
               public void mouseMoved(MouseEvent e) {}
           });
       }
       render(p,ct);
   }
  
   //渲染路径
   static void render(JPanel p,CityTest ct){
       Thread t = new Thread(ct);
       t.start();
       while(t.isAlive())
           Thread.yield();
       Graphics g = p.getGraphics();
       City x = ct.start;
       for(int i=0; i<ct.cs.length; i++){
           g.drawLine(x.x,x.y,ct.cs[ct.fin[i]].x,ct.cs[ct.fin[i]].y);
           x=ct.cs[ct.fin[i]];
       }
       g.drawLine(x.x,x.y,ct.end.x,ct.end.y);
   }
}
//城市类
class City{
   int id;//
   int x,y;//坐标
   City(int id){this.id=id;}
   //两城市之间的直线距离
   int getDist(City c){return (int)Math.sqrt(Math.pow(c.x-x,2)+Math.pow(c.y-y,2));}
}
