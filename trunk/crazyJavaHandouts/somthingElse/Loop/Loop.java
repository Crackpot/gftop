//比之前的方法效率有明显提高

public class Loop {
    public static void main(String[] args) {
        //求组成如下字符串的所有字符可能的组合
        String str = "abcde";
        //组合后字符串长度,当为元素无重复模式时，这个值要不大于元素个数
        int len = 2;
//        loop(new char[]{},str.toCharArray(),len);
        loopNoDup(new char[]{},str.toCharArray(),len);
    }

    //元素无重复
    public static void loopNoDup(char[] t,char[] a,int l){
        if(l>1){
            for(int i=0; i<a.length; i++){
                char[] b = new char[a.length-i-1];
                System.arraycopy(a,i+1,b,0,b.length);
                char[] c = new char[t.length+1];
                System.arraycopy(t,0,c,0,t.length);
                c[t.length]=a[i];
                loopNoDup(c,b,l-1);
            }
        }
        else {
            for(int i=0; i<a.length; i++){
                process(t,a[i]);
            }
        }
    }

    //元素可重复
    public static void loop(char[] t,char[] a,int l){
        if(l>1){
            for(int i=0; i<a.length; i++){
                char[] b = new char[t.length+1];
                System.arraycopy(t,0,b,0,t.length);
                b[t.length]=a[i];
                loop(b,a,l-1);
            }
        }
        else {
            for(int i=0; i<a.length; i++){
                process(t,a[i]);
            }
        }
    }

    private static void process(char[] t, char c) {
        for(char i:t)
            System.out.print(i);
        System.out.println(c);
    }
}
