import java.awt.*;

public class TestGridLayout {
	public static void main(String[] args) {
		Frame f = new Frame("计算器");
		// 设置Frame使用BorderLayout布局管理器
		f.setLayout(new BorderLayout());

		// 创建两个Panel对象
		Panel p1 = new Panel();
		Panel p2 = new Panel();

		// Panel中添加文本域
		p1.add(new TextField(20));

		// 将Panel添加在Frame北部
		f.add(p1, BorderLayout.NORTH);

		// 设置Panel使用GridLayout布局管理器
		p2.setLayout(new GridLayout(3, 5, 4, 4)); // 采用指定行数、列数、指定横向间距、纵向间距将容器分割成多个网格

		String[] name = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
				"+", "-", "*", "/", "." };
		
		// 向Panel中添加15个按钮
		for (int i = 0; i < 15; i++) {
			p2.add(new Button(name[i]));
		}

		// 默认将p2添加到f的中间
		f.add(p2);

		// 设置为最佳大小
		f.pack();
		// 设置为可见
		f.setVisible(true);
	}
}
