
import java.util.Arrays;
/**
 * Description:
 * <br/>Copyright (C), 2005-2008, Yeeku.H.Lee
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:
 * <br/>Date:
 * @author  Yeeku.H.Lee kongyeeku@163.com
 * @version  1.0
 */
class Person
{
	private int age;
	public Person(){}

	public Person(int age)
	{
		this.age = age;
	}
	public void setAge(int age)
	{
		this.age = age;
	}
	public int getAge()
	{
		 return this.age;
	}
}
public class TestFinalReference
{
	public static void main(String[] args) 
	{
		//final修饰数组变量，iArr是一个引用变量
		final int[] iArr = {5, 6, 12, 9};
		System.out.println(Arrays.toString(iArr));
		//对数组元素进行排序，合法
		Arrays.sort(iArr);
		System.out.println(Arrays.toString(iArr));
		//对数组元素赋值，合法
		iArr[2] = -8;
		System.out.println(Arrays.toString(iArr));
		//下面语句对iArr重新赋值，非法
		iArr = null;
		//final修饰Person变量，p是一个引用变量
		final Person p = new Person(45);
		//改变Person对象的age属性，合法
		p.setAge(23);
		System.out.println(p.getAge());
		//下面语句对p重新赋值，非法
		//p = null;
	}
}