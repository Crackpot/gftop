/**
 * P 92 
 * @author crackpot
 * 使用foreach而产生的错误
 */
public class TestForEachError {
	public static void main(String[] args) {
		String[] books = {
				"轻量级J2EE企业应用实战",
				"Struts2权威指南",
				"基于J2EE的Ajax宝典"};
		
		// 使用foreach循环来遍历数组元素，其中book将会自动迭代每个数组元素
		for (String book: books) {// 前者是后者的个体
			book = "Ruby on Rails 敏捷开发最佳实践";
			// 在该循环体中，再次对个体进行赋值将会使得内存中同名变量失效
			System.out.println(book);
		}
		System.out.println("##########");
		
		for (String book: books) {
			// 上循环体中再次对book赋值的语句不会对原有数组中的各个元素起作用，所以并未改变各元素的值。
			System.out.println(book);
		}
	}
}
