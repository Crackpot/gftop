import java.awt.*;
import java.awt.datatransfer.*;
import java.awt.event.*;
import java.io.IOException;
import javax.swing.*;

public class Pic{
    public static void main(String[] args) throws Exception {
        String imgPath = "http://hiphotos.baidu.com/ttbet/pic/item/aec13033b5877365ad4b5fc4.jpeg";
        Image img = new ImageIcon(new java.net.URL(imgPath)).getImage();
        P a = new P(img);
        P b = new P();
   P c = new P();
   P d = new P();
        JPanel p = new JPanel(new GridLayout(2,2,20,20));
        p.setBorder(BorderFactory.createEmptyBorder(20,20,20,20));
        p.add(a);
        p.add(b);p.add(c);p.add(d);
        Handler h = new Handler();
        a.setTransferHandler(h);
        b.setTransferHandler(h);
   c.setTransferHandler(h);
   d.setTransferHandler(h);
        JFrame f = new JFrame("DND demo");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(560,460);
        f.setLocationRelativeTo(null);
        f.setContentPane(p);
        f.setVisible(true);
    }
}
class P extends JComponent implements MouseListener,MouseMotionListener{
    private Image img;
    private MouseEvent eve;
    public P(){
        this(null);
    }
    public P(Image i){
        img=i;
        this.addMouseListener(this);
        this.addMouseMotionListener(this);
   setBorder(BorderFactory.createLineBorder(Color.gray));
    }
    public void setImage(Image img) {
        this.img=img;
        this.repaint();
    }
    public void paintComponent(Graphics gr){
        Graphics g = gr.create();
        if(img!=null){
            g.drawImage(img,0,0,this);
        }
        else{
            g.setColor(Color.white);
            g.fillRect(0,0,getWidth(),getHeight());
        }
        g.dispose();
    }
    public Image getImage(){return img;}
    public void mouseClicked(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
    public void mousePressed(MouseEvent e) {
        if(img==null)return;
        eve=e;e.consume();
    }
    public void mouseReleased(MouseEvent e) {eve=null;}
    public void mouseDragged(MouseEvent e) {
        if(img==null)return;
        if(eve!=null)
            e.consume();
        int action = TransferHandler.MOVE;
        int dx = Math.abs(eve.getX()-e.getX());
        int dy = Math.abs(eve.getY()-e.getY());
        if(dx>5||dy>5){
            JComponent c = (JComponent)e.getSource();
            TransferHandler handler = c.getTransferHandler();
            handler.exportAsDrag(c, eve, action);
            eve=null;
        }
    }
    public void mouseMoved(MouseEvent e) {}
}
class Handler extends TransferHandler{
    private DataFlavor fx = DataFlavor.imageFlavor;
    private P src;
    private boolean shouldMove;

    public boolean importData(JComponent c,Transferable t){
        if(src==c)
            return false;
        if(this.canImport(c,t.getTransferDataFlavors())){
            P tmp = (P)c;
            try{
                Image img = ((I)t.getTransferData(fx)).i;
                tmp.setImage(img);
                shouldMove=true;
                return true;
            }catch(Exception e){e.printStackTrace();}
        }
        return false;
    }
    public void exportDone(JComponent c,Transferable data,int action){
        if(shouldMove&&action==MOVE){
            src.setImage(null);
        }
        src=null;
    }
    public int getSourceActions(JComponent c){
        return MOVE|COPY;
    }
    public boolean canImport(JComponent c,DataFlavor[] fs){
        for(int i=0; i<fs.length; i++)
            if(fx.equals(fs[i]))
                return true;
        return false;
    }
    public Transferable createTransferable(JComponent c){
        src = (P)c;
        return new Transfer(src);
    }
    class Transfer implements Transferable{
        private I i;
        private Transfer(P p){
            i=new I();
            i.i=p.getImage();
        }
        public Object getTransferData(DataFlavor f)
                throws UnsupportedFlavorException, IOException {
            if(this.isDataFlavorSupported(f)){
                return i;
            }
            throw new UnsupportedFlavorException(f);
        }
        public DataFlavor[] getTransferDataFlavors() {
            return new DataFlavor[]{fx};
        }
        public boolean isDataFlavorSupported(DataFlavor f) {
            return fx.equals(f);
        }
    
    }
    class I{
        Image i;
    }
}

