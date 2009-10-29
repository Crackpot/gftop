import javax.sound.midi.*;

public class MiniMiniMusicApp {
    public static void main(String[] args) {
        MiniMiniMusicApp mini = new MiniMiniMusicApp();
        mini.play();
    }// close method main
    public void play() {
        try {
            // 步骤1 取得Sequencer并将其打开。
            Sequencer player = MidiSystem.getSequencer();
            player.open();
            // 步骤2 创建新的Sequence。
            Sequence seq = new Sequence(Sequence.PPQ, 4);
            // 步骤3 从Sequencer中创建新的Track。
            Track track = seq.createTrack();//要求取得Track
            // 步骤4 填入MidiEvent并让Sequencer播放。
            // 对Track加入几个MidiEvent，要主义的是setMessage()的参数，以及MidiEvent的constructor。
            ShortMessage a = new ShortMessage();
            a.setMessage(144, 1, 44, 100);
            MidiEvent noteOn = new MidiEvent(a, 1);
            track.add(noteOn);

            ShortMessage b = new ShortMessage();
            b.setMessage(128, 1, 44, 100);
            MidiEvent noteOff = new MidiEvent(b, 16);
            track.add(noteOff);
            player.setSequence(seq);// 将Sequence送到Sequencer上。
            // 步骤5 按下播放键
            player.start();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }// close method play
}// close class MiniMiniMusicApp
