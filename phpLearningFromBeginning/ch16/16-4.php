<?php
$file = './test/readme.txt';

try
{
    if(is_dir($file))
    {
        echo '��⵽Ŀ¼';
    }
    else
    {
        //�����쳣���󣬴�����Ϣ����Exception��ĳ�Ա����getMessage()����
        throw new Exception('δ�ҵ���Ŀ¼���ļ�');
    }
}
catch(Exception $e)
{
    echo '�����쳣: ' . $e->getMessage();
    echo '<br/><br/>';
    echo '���������ļ���'. $e->getFile();
    echo '<br/>===============================';
    echo '<br/>';
}

echo '����ִ�����';
?>
