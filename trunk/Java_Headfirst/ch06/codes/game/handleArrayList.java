import java.util.ArrayList;
public class handleArrayList {
    public static void main(String[] args) {
        // 这个"<>"，这代表创建出Egg类型的List
        ArrayList<Egg> myList = new ArrayList<Egg>();
        // 加入元素
        Egg s = new Egg();
        myList.add(s);
        // 再加入元素
        Egg b = new Egg();
        // 查询大小
        myList.add(b);
        int theSize = myList.size();
        System.out.println("ArrayList的长度为：" + theSize);
        // 查询特定元素
        boolean isIn = myList.contains(s);
        // 查询特定元素的位置
        int idx = myList.indexOf(b);
        // 判断集合是否为空
        boolean empty = myList.isEmpty();
        if (empty) {
            System.out.println("ArrayList为空！");
        } else {
            System.out.println("ArrayList不为空！");
        }
        // 删除元素
        myList.remove(s);
    }
}

class Egg {
    private String color;
    private int weight;

    public void setColor(String aColor) {
        color = aColor;
    }
    public String getColor() {
        return this.color;
    }

    public void setWeight(int aWeight) {
        weight = aWeight;
    }
    public int getWeight() {
        return this.weight;
    }
}
