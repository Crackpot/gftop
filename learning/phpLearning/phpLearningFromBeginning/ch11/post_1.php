<?php
$file_name = 'contents/200712/2-215307.txt';    //存储日志内容的文件

if(file_exists($file_name))                     //打开文件前需要判断文件是否存在
{
    $fp = @fopen($file_name, 'r');              //以只读方式打开文件
    if($fp)
    {
        flock($fp, LOCK_SH);                    //文件加锁
        $result = fread($fp, 1024);             //读出文件中的内容
    }
    flock($fp, LOCK_UN);                        //解锁文件
    fclose($fp);
}

//将字符串$result的内容按“|”分割后存入数组$content_array
$content_array = explode('|', $result);

//以下代码将日志内容输出
echo '<h1>我的BLOG</h1>';
echo '<b>日志标题：</b>'.$content_array[0];
echo '<br/><b>发布时间：</b>'.date('Y-m-d H:i:s',$content_array[1]);
echo '<hr>';
echo $content_array[2];
?>
