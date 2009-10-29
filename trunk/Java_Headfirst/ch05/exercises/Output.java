class Output {
    public static void main(String[] args) {
        Output o = new Output();
        o.go();
    }
    void go() {
        int y = 7;
        for(int x = 1; x < 8; x++) {
            y++;
            if (x > 4) {
                System.out.print(++y + " ");
            }
            if (y > 14) {
                System.out.println(" x = " + x);
                break;
            }
        }
    }
}
/*
 * x从1增加到大于4至少要执行4次循环，而循环的同时y也在增加，此时y的值为7+1+4=12，而当输出y时，又增加了一次，为13
 * */
