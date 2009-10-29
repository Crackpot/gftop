class BooksTestDrive {
    public static void main(String[] args) {

        Books [] myBooks = new Books[3];// 创建Books数组，虽然有了对Books的引用，但是缺少了实际的Books对象
        int x = 0;

        myBooks[0] = new Books();// 创建新的Books对象并将它们赋值给数组元素
        myBooks[0].title = "The Grapes of Java";
        myBooks[0].author = "bob";

        myBooks[1] = new Books();
        myBooks[1].title = "The Java Gatsby";
        myBooks[1].author = "sue";

        myBooks[2] = new Books();
        myBooks[2].title = "The Java Cookbook";
        myBooks[2].author = "ian";

        while (x < 3) {
            System.out.print(myBooks[x].title);
            System.out.print(" by ");
            System.out.println(myBooks[x].author);
            x = x + 1;
        }
    }
}
