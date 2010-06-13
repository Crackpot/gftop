import java.util.*;

public class DotCom {// 我们把类的名称从SimpleDotCom改成DotCom，但程序代码和上一章相同

    // DotCom的实例变量：
    private ArrayList<String> locationCells;// 保存位置的ArrayList
    private String name;// DotCom的名称


    public void setLocationCells(ArrayList<String> loc) {// 更新DotCom位置的setter方法
        locationCells = loc;
    }// close setLocationCells method

    public void setName(String n) {// 基本的setter方法
        name = n;
    }

    public String checkYourself(String userInput) {
        String result = "miss";// 创建出保存返回结果的变量，以miss作为默认值

        int index = locationCells.indexOf(userInput);// 判别玩家猜测值是否出现在ArrayList中，没有的话返回-1

        if (index >= 0) {// 如果索引值大于或等于0，命中
            locationCells.remove(index);// 删除已经命中的格子

            if (locationCells.isEmpty()) {// 如果全部命中清空，那就表示击沉了
                result = "kill";
                System.out.println("Ouch! You sunk " + name + "  :( ");
            } else {
                result = "hit";
            } // close if
        }// close outer if
        return result;// 将结果返回给调用方
    }// close method
}// close class

/*
 * 去除bug的方案：
 * 方案1：
 *     可以使用第二个数组，每当玩家猜中某一格时，我们就把相对的那一格设定为true，之后每次猜中都要检查是否在之前就已经被猜过了。
 * 方案2：
 *     我们可以只动用原来的数组，办法是将任何被命中的格子改为-1，这样就只需要维护与检查一个数组。
 * 方案3：
 *     在命中某个格子时就把它删除掉，因此格子就会越来越少。但是数组无法改变大小，因此我们必须作出新的数组并拷贝旧数组的值。
 * 如果数组能缩小的话，方案三会更好，如此就不用拷贝并重新赋值引用。
 * 其实真的有这样的集合，但它不是数组，而是个ArrayList。它是Java函数库中的另一个类
 * */

/*
 * ArrayList的说明：
 *     add(Object elem)
 *         向list中加入对象参数
 *     remove(int index)
 *         在索引参数中移除对象
 *     remove(Object elem)
 *         移除该对象
 *     contains(Object elem)
 *         如果和对象参数匹配返回"true"
 *     isEmpty()
 *         如果list中没有元素返回"true"
 *     indexOf(Object elem)
 *         返回对象参数的索引或-1
 *     size()
 *         返回list中元素的个数
 *     get(int index)
 *         返回当前索引参数的对象
 * */
