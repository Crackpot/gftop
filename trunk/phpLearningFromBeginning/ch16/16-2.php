<?php
try
{
    $error = '�׳��쳣��Ϣ����������try��<br/>';
    if(is_dir('./test'))
    {
        echo '��⵽../ch16��һ��Ŀ¼';
        echo '<br/>';
        echo '���ܼ���������һЩ����';
        echo '<br/>';
        echo '....';
        echo '<br/>';
    }
    else
    {
        throw new Exception($error,12345);
    }
    echo '����throw�쳣�Ļ������д��벻��ִ�У�ת��ִ��catch��<br/>';
}
catch(Exception $e)
{
    echo '�����쳣: ' . $e->getMessage() . "<br/>������룺" . $e->getCode().'<br/>';    //��ʾ$error��123456
    echo '<br/>';
}

echo '����ִ��';
?>