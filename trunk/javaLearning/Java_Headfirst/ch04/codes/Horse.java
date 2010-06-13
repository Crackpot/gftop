class Horse {

    // 实例变量是声明在类中而不是方法中
    private double height = 15.2;
    private String breed;
    
    public void setHeight(double aheight) {
        height = aheight;
    }
    public double getHeight() {
        return height;
    }

    public void setBreed (String abreed) {
        breed = abreed;
    }
    public String getBreed() {
        return breed;
    }
}
