<?php
$file = "data.txt"; 
$content = "���ݱ���\r\n���ݵ�һ��\r\n���ݵڶ���";    //Ҫд�������

if(!$fp = fopen($file,'a'))                           //���ļ�$fileʱ��ʹ��׷��ģʽ����ʱ�ļ�ָ������ļ���ʼ��
{
    echo "���ļ�$fileʧ�ܣ�";
    exit;
}

if(fwrite($fp,$content) === FALSE)                    //������д���ļ�
{
    echo "д���ļ�ʧ�ܣ�";
    exit;
}

echo "д���ļ��ɹ���";
fclose($fp);
?>