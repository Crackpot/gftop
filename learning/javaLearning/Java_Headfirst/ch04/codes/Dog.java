class Dog {
    int size;
    String name;

    void bark() {
        if (size > 60) {
            System.out.println("Size : " + size + " => Wooof! Wooof!");
        } else if (size > 14) {
            System.out.println("Size : " + size + " => Ruff! Ruff!");
        } else {
            System.out.println("Size : " + size + " => Yip! Yip!");
        }
    }
}
