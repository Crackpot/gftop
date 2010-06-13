class SoundPlayer {
    public void playSound(String title) {
        System.out.println("正在播放 : " + title);
    }
}

public class Song {

    /*
     * 实例变量的值会影响到play()方法的行为
     * */
    String title;

    /*
     * 构造函数
     * */
    public Song(String t) {
        title = t;
    }

    /*
     * 播放方法
     * */
    public void play() {
        SoundPlayer player= new SoundPlayer(); //创建副类对象
        player.playSound(title); //调用类SoundPlayer中的方法playSound，title的值会决定play()方法所播放的内容。
    }

    /*
     * 主方法
     * */
    public static void main(String[] args) {
        Song SongInstance = new Song("在那遥远的地方");//创建主类对象
        SongInstance.play();//激活方法
        Song SongInstance1 = new Song("吐鲁番的葡萄熟了");//创建主类对象
        SongInstance1.play();//激活方法
        Song SongInstance2 = new Song("敖包相会");//创建主类对象
        SongInstance2.play();//激活方法

    }
}
