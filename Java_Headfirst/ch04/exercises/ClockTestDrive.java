class ClockTestDrive {
    public static void main(String[] args) {
        Clock c = new Clock();
        c.setTime("22:36:10");
        String tod = c.getTime();
        System.out.println("The time is : " + tod);
    }
}
