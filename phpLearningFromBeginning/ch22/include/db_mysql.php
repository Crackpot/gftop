<?php
$h="localhost";  //数据库服务器名称
$u="root";       //数据库用户名
$p="admin";      //数据库密码
$db = "mybbs";   //数据库名称

function db_connect($h,$p,$u,$db)   //连接数据库
{
    if(!($conn = mysql_connect($h, $u, $p))) 
        return false;
    
    //如果没有该数据库，则返回失败。
    if(!mysql_select_db($db))
    {
        mysql_close($conn);
        return false;
    }
    else
        return $conn;
}

function close_db($conn)            //断开与数据库的连接
{
    mysql_close($conn);
}
?>