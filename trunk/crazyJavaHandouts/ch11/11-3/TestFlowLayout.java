import java.awt.*;

public class TestFlowLayout {
	public static void main(String[] args) {
		Frame f = new Frame("测试窗口");

		// 设置Frame容器使用FlowLayout布局管理器
		f.setLayout(new FlowLayout(FlowLayout.LEFT, 20, 5));

		// 向窗口中添加10个按钮
		for (int i = 0; i < 10; i++) {
			f.add(new Button("按钮" + i));
		}

		// 设置窗口为最佳大小
		f.pack();

		// 将窗口显示出来
		f.setVisible(true);
	}
}
