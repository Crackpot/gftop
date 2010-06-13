import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
//Download by http://www.codefans.net
public class OperationButton extends Button
{
  String 运算符号;
  public OperationButton(String s)
   {
    super(s);
    运算符号=s;
    setForeground(Color.red);
   }
  public String get运算符号()
   {
     return 运算符号;
   }
}

