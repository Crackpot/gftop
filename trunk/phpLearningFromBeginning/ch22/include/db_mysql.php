<?php
$h="localhost";  //���ݿ����������
$u="root";       //���ݿ��û���
$p="admin";      //���ݿ�����
$db = "mybbs";   //���ݿ�����

function db_connect($h,$p,$u,$db)   //�������ݿ�
{
    if(!($conn = mysql_connect($h, $u, $p))) 
        return false;
    
    //���û�и����ݿ⣬�򷵻�ʧ�ܡ�
    if(!mysql_select_db($db))
    {
        mysql_close($conn);
        return false;
    }
    else
        return $conn;
}

function close_db($conn)            //�Ͽ������ݿ������
{
    mysql_close($conn);
}
?>