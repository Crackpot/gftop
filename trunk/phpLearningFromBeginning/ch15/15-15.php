<?php
$str_arr = array(
"IAMEVERYSORRY",
"���ֱ�̣���������",
"PHP���",
"1997����ۻع�",
"Ӣ��ѧϰABC",
"123456789"
);

$patt_ch = chr(0xa1) . "-" . chr(0xff);

foreach ($str_arr as $str)
{
    echo "�ַ���'$str' ��";
    if (preg_match("/^[$patt_ch]+$/", $str))
    {
        echo "<b>��ȫ����</b>";
        echo "<br>";
        echo "<br>";
    }
    else
    {
        echo "����ȫ����";
        echo "<br>";
        echo "<br>";
    }
}
?>