<?php
$dir_name = "tmp_data";

if(mkdir($dir_name))    //�ڵ�ǰĿ¼�´���Ŀ¼tmp_data
{
    echo "Ŀ¼".$dir_name."�����ɹ���";
    
    //��Ŀ¼tmp_data�д���һ���ļ�tmp.txt����������д��һЩ����
    if($fp = fopen($dir_name."/tmp.txt",'a'))
    {
        if(fwrite($fp,"Put Some Contenets into File."))
        {
            echo "<hr>";
            echo "��Ŀ¼".$dir_name."�´����ļ�tmp.txt";
        }
    }
}
else
{
    echo "����Ŀ¼ʧ�ܣ�";
    exit;
}
echo "<hr>";

if(rmdir($dir_name))    //����ɾ��Ŀ¼tmp_data
{
    echo "ɾ��Ŀ¼".$dir_name."�ɹ���";
}
else
{
    echo "ɾ��Ŀ¼ʧ�ܣ�";
    exit;
}
?>