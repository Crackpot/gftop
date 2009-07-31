
import java.awt.*;
import static java.awt.BorderLayout.*;

/**
 * Description:
 * <br/>Copyright (C), 2005-2008, Yeeku.H.Lee
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:
 * <br/>Date:
 * @author  Yeeku.H.Lee kongyeeku@163.com
 * @version  1.0
 */
public class TestBorderLayout2
{
	public static void main(String[] args) 
	{
		Frame f = new Frame("测试窗口");
		//设置Frame容器使用BorderLayout布局管理器
		f.setLayout(new BorderLayout(30, 5));
		f.add(new Button("南") , SOUTH);
		f.add(new Button("北") , NORTH);
		//创建一个Panel对象
		Panel p = new Panel();
		//相Panel对象中添加两个组件
		p.add(new TextField(20));
		p.add(new Button("单击我"));
		//默认添加到中间
		f.add(p);
		f.add(new Button("东") , EAST);
		//f.add(new Button("西") , WEST);
		//设置窗口为最佳大小
		f.pack();
		//将窗口显示出来（Frame对象默认处于隐藏状态）
		f.setVisible(true);
	}
}
