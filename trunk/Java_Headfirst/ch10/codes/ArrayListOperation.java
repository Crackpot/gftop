import java.util.ArrayList;

public class ArrayListOperation {

    /*
     * 静态方法
     * */

    /*
     * 增加项
     * */
    public static ArrayList add(ArrayList list, Object elem) {
        list.add(elem);
        System.out.println("向ArrayList对象添加了" + elem);
        return list;
    }

    /*
     * 删除项
     * 以下两个方法同名但参数不同，是一个重载实例
     * */
    public static ArrayList remove(ArrayList list, int index) {
        try {
            list.remove(index);
            System.out.println("对ArrayList对象移除了索引为" + index + "的项");
        } catch (Exception ex) {
            //System.out.println(ex);
            System.out.println("在对ArrayList对象移除索引为" + index + "的项时出现错误：无此索引!");
        }
        return list;
    }
    public static ArrayList remove(ArrayList list, Object elem) {
        if (list.contains(elem)) {
            list.remove(elem);
            System.out.println("对ArrayList对象移除了项" + elem);
        } else {
            System.out.println("在对ArrayList对象移除项" + elem + "时出现错误：无此项!");
        }
        return list;
    }

    /*
     * 包含项
     * */
    public static boolean contains(ArrayList list, Object elem) {
        if (list.contains(elem)) {
            System.out.println("对象中包含项" + elem);
        } else {
            System.out.println("对象中不包含项" + elem);
        }
        return list.contains(elem);
    }

    /*
     * 为空
     * */
    public static boolean isEmpty(ArrayList list) {
        if (list.isEmpty()) {
            System.out.println("对象为空");
        } else {
            System.out.println("对象不为空");
        }
        return list.isEmpty();
    }

    /*
     * 取项的索引值
     * */
    public static int indexOf(ArrayList list, Object elem) {
        if (list.indexOf(elem) != -1) {
            System.out.println("对象中的项" + elem + "的索引为：" + list.indexOf(elem));
        } else {
            System.out.println("对象中不存在项" + elem);
        }
        return list.indexOf(elem);
    }

    /*
     * 求大小
     * */
    public static int size(ArrayList list) {
        System.out.println("对象的大小为：" + list.size());
        return list.size();
    }

    /*
     * 取相应索引的项
     * */
    public static Object get(ArrayList list, int index) {
        try {
            System.out.println("对象中索引为" + index + "的项为：" + list.get(index));
            return list.get(index);
        } catch (Exception ex) {
            System.out.println("在对ArrayList对象移除索引为" + index + "的项时出现错误：无此索引!");
            return null;
        }
    }

    /*
     * 遍历ArrayList
     * */
    public static void gets(ArrayList list) {
        int index = 0;
        while (index < 100) {
            try {
                System.out.println("对象中索引为" + index + "的项为：" + list.get(index));
                index++;
            } catch (Exception ex) {
                break;
            }
        }

    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        int x = 32;
        ArrayList list = new ArrayList();

        add(list,55);
        add(list,"Crackpot");
        add(list,null);
        add(list,4.31);

        remove(list,1);
        remove(list,"hehe");

        contains(list,"Crackpot");

        isEmpty(list);

        indexOf(list,"haha");

        size(list);

        get(list,5);
        gets(list);
    }
}

/*
 * ArrayList方法摘要
 *     boolean    add(E o)
 *         将指定的元素追加到此 List 的尾部（可选操作）。
 *     void   add(int index, E element)
 *         在此列表中指定的位置插入指定的元素（可选操作）。
 *     boolean    addAll(int index, Collection<? extends E> c)
 *         将指定 collection 中的所有元素插入此列表的指定位置（可选操作）。
 *     void   clear()
 *         从此 collection 中移除所有元素（可选操作）。
 *     boolean    equals(Object o)
 *         将指定的对象与此列表进行相等性比较。
 *     abstract  E     get(int index)
 *         返回此列表中指定位置处的元素。
 *     int    hashCode()
 *         返回此列表的哈希码值。
 *     int    indexOf(Object o)
 *         返回此列表中首次出现指定元素的索引，如果列表中不包含此元素，则返回 -1。
 *     Iterator<E>    iterator()
 *         返回以正确顺序在此列表的元素上进行迭代的迭代器。
 *     int    lastIndexOf(Object o)
 *         返回此列表中最后出现指定元素的索引，如果列表中不包含此元素，则返回 -1。
 *     ListIterator<E>    listIterator()
 *         返回此列表中的元素的迭代器（按适当顺序）。
 *     ListIterator<E>    listIterator(int index)
 *         从列表中的指定位置开始，返回此列表中的元素的列表迭代器（按适当顺序）。
 *     E  remove(int index)
 *        移除此列表中指定位置处的元素（可选操作）。
 *     protected  void     removeRange(int fromIndex, int toIndex)
 *        从此列表中移除其索引在 fromIndex（包括）和 toIndex（不包括）之间的所有元素。
 *     E  set(int index, E element)
 *        将此列表中指定位置的元素替换为指定的元素（可选操作）。
 *     List<E>    subList(int fromIndex, int toIndex)
 *        返回此列表 fromIndex（包括）和 toIndex（不包括）之间部分的视图。*
 * */
