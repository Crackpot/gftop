import java.lang.Math;

public class Laundry {
    static void doLaundry(String clothType) throws ClothingException, PantsException, LingerieException, ShirtException, TeeShirtException, DressShirtException, UniformException {// 洗涤 静态方法
        System.out.println("顾客您好，欢迎光临洗衣房！\n您要洗涤" + clothType);
        if ("Pants".equals(clothType)) {// 裤子
            throw new PantsException();
        } else if ("Uniform".equals(clothType)) {// 制服
            throw new UniformException();
        } else if ("Lingerie".equals(clothType)) {// 女士内衣
            throw new LingerieException();
        } else if ("TeeShirt".equals(clothType)) {// TeeShirt
            throw new TeeShirtException();
        } else if ("DressShirt".equals(clothType)) {// DressShirt
            throw new DressShirtException();
        } else if ("Shirt".equals(clothType)) {// Shirt
            throw new ShirtException();
        } else if ("Clothing".equals(clothType)) {// Clothing
            throw new ClothingException();
        }
        System.out.println("洗涤完成，欢迎再次惠顾！");// 这里这一行不会执行
    }// close method doLaundry
    public static void main(String[] args) {
        String[] clothType = {"Clothing", "Pants", "Lingerie", "Uniform", "TeeShirt", "DressShirt", "Shirt"};
        /*
         * 有多个catch块时要从小排到大，否则父类会将子类屏蔽
         * 不能把大篮子放在小篮子上面！
         * */
        try {
            int typeIndex;
            double randomSeed = Math.random();// 产生正的大于或等于0.0，小于1.0的double值。 
            typeIndex = (int)(randomSeed * 7);// 将下标控制到0到6
            System.out.println(String.format("系统产生的随机数是:%.2f\t衣服种类为%d",randomSeed,typeIndex));
            doLaundry(clothType[typeIndex]);
        } catch (PantsException pex) {// 裤子
            System.out.println("捕获到PantsException");
        } catch (LingerieException pex) {// 女士内衣
            System.out.println("捕获到LingerieException");
        } catch (UniformException uex) {// 制服
            System.out.println("捕获到UniformException");
        } catch (TeeShirtException pex) {// TeeShirt
            System.out.println("捕获到TeeShirtException");
        } catch (DressShirtException pex) {// DressShirt
            System.out.println("捕获到DressShirtException");
        } catch (ShirtException sex) {// TeeShirtException、DressShirtException的父类
            System.out.println("捕获到ShirtException");
        } catch (ClothingException sex) {// PantsException、LingerieException、UniformException、ShirtException的父类
            System.out.println("捕获到ClothingException");
        } finally {// 不管怎么样都要执行的部分
            System.out.println("洗涤完成，欢迎再次惠顾！");
        }
        return;
    }// close method main
}// close class ClothingExceptionTestDrive
