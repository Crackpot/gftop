class Vet { //诊断类
    public void giveShot(Animal animal) { //给宠物打针
        /*
         * 本函数的参数可以是用任何Animal的类型对象来传入。执行到makeNoise()的时候，不管它引用的对象到底是什么，该对象都会执行makeNoise()。
         * */
        animal.makeNoise();
        System.out.println();
    }
}

public class PetOwner { //宠物主人类

    public void start() {
        /*
         * giveShot这个方法可以取用任何一种Animal。只要所传入的是Animal的子类它都能执行。
         * */
        Vet VetInstance = new Vet(); //创建诊断对象
        Dog DogInstance = new Dog("狗"); 
        VetInstance.giveShot(DogInstance); // 给狗打针
        Hippo HippoInstance = new Hippo("河马");
        VetInstance.giveShot(HippoInstance); // 给河马打针
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        PetOwner PetOwnerInstance = new PetOwner(); //创建对象
        PetOwnerInstance.start(); //调用start方法
    }
}
