class Exercise1b {
    public static void main(String[] args) {
        int x = 10;
        while (x > 1) {
            x = x - 1;
            if (x > 5) {
                System.out.println("big x:" + x);
            }
            if (x < 3) {
                System.out.println("small x:" + x);
            }
        }
    }
}
