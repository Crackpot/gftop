public class MushroomTestDrive {
    public static void main(String[] args) {
        Mushroom[] MushroomInstance = new Mushroom[8];
        MushroomInstance[0] = new Mushroom();
        MushroomInstance[1] = new Mushroom(21);
        MushroomInstance[2] = new Mushroom(true);
        MushroomInstance[3] = new Mushroom(false);
        MushroomInstance[4] = new Mushroom(true,22);
        MushroomInstance[5] = new Mushroom(false,23);
        MushroomInstance[6] = new Mushroom(24,true);
        MushroomInstance[7] = new Mushroom(25,false);
    }
}
