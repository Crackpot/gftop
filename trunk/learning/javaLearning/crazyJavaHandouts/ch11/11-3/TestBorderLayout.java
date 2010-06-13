import java.awt.*;

public class TestBorderLayout {
	public static void main(String[] args) {
		Frame f = new Frame("测试窗口");
		// 设置Frame容器使用BorderLayout布局管理器
		f.setLayout(new BorderLayout(30, 5)); // 水平间距为30，垂直间距为5

		// 向窗口中添加对象
		f.add(new Button("南"), BorderLayout.SOUTH);
		f.add(new Button("北"), BorderLayout.NORTH);
		// 默认添加在中间
		f.add(new Button("中"));
		f.add(new Button("东"), BorderLayout.EAST);
		f.add(new Button("西"), BorderLayout.WEST);
		// 设置窗口为最佳大小
		f.pack();
		f.setVisible(true);
	}
}
