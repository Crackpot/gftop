
import java.io.*;
/**
 * Description:
 * <br/>Copyright (C), 2005-2008, Yeeku.H.Lee
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:
 * <br/>Date:
 * @author  Yeeku.H.Lee kongyeeku@163.com
 * @version  1.0
 */
public class AccessExceptionMsg
{
	public static void main(String[] args) 
	{
		try
		{
			FileInputStream fis = new FileInputStream("a.txt");
		}
		catch (IOException ioe)
		{
			System.out.println(ioe.getMessage());
			ioe.printStackTrace();
		}
	}
}
