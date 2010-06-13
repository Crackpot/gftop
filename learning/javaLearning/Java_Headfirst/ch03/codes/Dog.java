class Dog {
    String name;
    public static void main(String[] args){
        // 创建Dog对象
        Dog dog1 = new Dog();
        dog1.bark();// 终端输出 null says Ruff!
        dog1.name = "Bart";

        // 创建Dog数组
        Dog[] myDogs = new Dog[3];

        // 关门放狗
        myDogs[0] = new Dog();
        myDogs[1] = new Dog();
        myDogs[2] = dog1;// 一台电视有两个遥控器，指向名为Bart的狗

        // 通过数组应用存取Dog
        myDogs[0].name = "Fred";
        myDogs[1].name = "Marge";

        // myDogs[2]的名字是？
        System.out.print("last dog's name is ");
        System.out.println(myDogs[2].name);

        // 逐个对Dog执行bark()
        int x = 0;
        while (x < myDogs.length) {// 求得数组的长度，即元素的数目
            myDogs[x].bark();
            x = x + 1;
        }
    }
    public void bark() {
        System.out.println(name + " says Ruff!");
    }
}
