<?php
$dir = "D:\files";

//��Ŀ¼$dir������Ŀ¼�����������$dh
if($dh = opendir($dir))
{
    //ͨ��whileѭ����ʹ�ú���readdir��ȡ�ļ���
    while(($file_name = readdir($dh)) !== FALSE)
    {
        echo "file name: ".$file_name;
        echo "<br/>";
        echo "<br/>";
    }
    
    //������ɺ󣬹ر�Ŀ¼���$dh
    closedir($dh);
}
?>