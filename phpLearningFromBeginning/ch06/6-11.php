<?php
$dir_name = "tmp_data";
$new_file = "tmp_new.txt";

if(!copy($dir_name."/tmp.txt",$new_file))
{
    echo "Copy �ļ�tmp.txtʧ��";
    exit;
}

echo "�ļ�tmp.txt�����ɹ�";
echo "<br/>";
echo "<br/>";
echo "<hr>";
echo "<br/>";

if(unlink($new_file))
{
    echo "�ļ�".$new_file."ɾ���ɹ�";
}
else
{
    echo "�ļ�".$new_file."ɾ��ʧ��";
}
?>