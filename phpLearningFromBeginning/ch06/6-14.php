<?
echo "<H3>ͨ��httpЭ����ļ�</H3>";
echo "<br/>";

//ͨ�� http Э����ļ�
if(!($file = fopen("http://localhost/ch06/server_data.txt", "r")))
{
    echo "�ļ����ܴ�";
    exit;
}
while(!feof($file))
{
    $line = fgetss($file, 255);    //���ж�ȡ�ļ��е�����
    echo $line;
    echo "<br/>";
}

fclose($file);                     //�ر��ļ��ľ��
?>