<?php
$file_name = 'contents/200712/2-215307.txt';    //�洢��־���ݵ��ļ�

if(file_exists($file_name))                     //���ļ�ǰ��Ҫ�ж��ļ��Ƿ����
{
    $fp = @fopen($file_name, 'r');              //��ֻ����ʽ���ļ�
    if($fp)
    {
        flock($fp, LOCK_SH);                    //�ļ�����
        $result = fread($fp, 1024);             //�����ļ��е�����
    }
    flock($fp, LOCK_UN);                        //�����ļ�
    fclose($fp);
}

//���ַ���$result�����ݰ���|���ָ���������$content_array
$content_array = explode('|', $result);

//���´��뽫��־�������
echo '<h1>�ҵ�BLOG</h1>';
echo '<b>��־���⣺</b>'.$content_array[0];
echo '<br/><b>����ʱ�䣺</b>'.date('Y-m-d H:i:s',$content_array[1]);
echo '<hr>';
echo $content_array[2];
?>
