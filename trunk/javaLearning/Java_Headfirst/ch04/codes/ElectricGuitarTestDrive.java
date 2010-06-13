class ElectricGuitarTestDrive {
    public static void main(String[] args) {

        ElectricGuitar eg = new ElectricGuitar();

        eg.setBrand("Yamaha");
        System.out.println("The brand of the ElectricGuitar is " + eg.getBrand());

        eg.setNumOfPickups(5);
        System.out.println("The numOfPickups of the ElectricGuitar is " + eg.getNumOfPickups());

        eg.setRockStarUsesIt(true);
        if (eg.getRockStarUsesIt()) {
            System.out.println("Rock star uses the ElectricGuitar");
        } else {
            System.out.println("Rock star donot uses the ElectricGuitar");
        }
    }
}
