import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
//Download by http://www.codefans.net
public class NumberButton extends Button
{
  int number;
  public NumberButton(int number)
   {
    super(""+number);
    this.number=number;
    setForeground(Color.blue);
   }
  public int getNumber()
   {
     return number;
   }
}


