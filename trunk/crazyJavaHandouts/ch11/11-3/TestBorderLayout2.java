import java.awt.*;

public class TestBorderLayout2 {
	public static void main(String[] args) {
		Frame f = new Frame("测试窗口");
		// 设置Frame容器使用BorderLayout布局管理器
		f.setLayout(new BorderLayout(30, 5));
		f.add(new Button("南"), BorderLayout.SOUTH);
		f.add(new Button("北"), BorderLayout.NORTH);

		// 创建一个Panel对象
		Panel p = new Panel();

		// 向Panel添加两个部件
		p.add(new TextField(20));
		p.add(new Button("单击我"));

		// 默认添加Panel到Frame中间
		f.add(p);

		// 添加右边按钮
		f.add(new Button("东"), BorderLayout.EAST);

		// 设置窗口为最佳大小
		f.pack();

		// 设置为可见
		f.setVisible(true);
	}
}
