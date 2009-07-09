<?php
$file = './test/readme.txt';

try
{
    if(is_dir($file))
    {
        echo '检测到目录';
    }
    else
    {
        //创建异常对象，错误信息将有Exception类的成员函数getMessage()返回
        throw new Exception('未找到该目录或文件');
    }
}
catch(Exception $e)
{
    echo '捕获异常: ' . $e->getMessage();
    echo '<br/>===============================';
    echo '<br/>';
}

echo '程序执行完毕';
?>
