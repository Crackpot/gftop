<?php
$str_arr = array(
"PHP �������Web�ű�����",
"Perl���ı������ܺ�ǿ��"
);

foreach($str_arr as $str)
{
    //ģʽ����������������"i" ��ʾƥ��ʱ�����ִ�Сд��ĸ
    if(preg_match("/php/i", $str))
    {
        echo "���ַ���' $str '���ҵ���'php'��ƥ��";
        echo "<br/>";
        echo "<br/>";
    }
    else
    {
        echo "���ַ���' $str '��<b>δ</b>�ҵ���'php'��ƥ��";
        echo "<br/>";
        echo "<br/>";
    }
}
?>