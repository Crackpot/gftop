<?php
    echo "<h3>服务器变量 $_SERVER 举例：</h3>";
    $a = "test string";
    echo "通过\$GLOBALS来取变量值：".$GLOBALS['a']."<br/>";

    echo "当前执行脚本的文件名：".$_SERVER['PHP_SELF']."<br/>"; // 获取当前正在执行脚本文名

    echo "当前执行脚本所在的根目录：".$_SERVER['DOCUMENT_ROOT']."<br/>";

    echo "当前执行脚本的的绝对路径：".$_SERVER['SCRIPT_FILENAME']."<br/>";

    echo "请求页面时通信协议的名称和版本：".$_SERVER['SERVER_PROTOCOL']."<br/>"; // 请求页面时通信协议的名称和版本。例如，“HTTP/1.0”。

    echo "请求开始的时间戳：".$_SERVER['REQUEST_TIME']."<br/>" // 请求开始时的时间戳。从 PHP 5.1.0 起有效。和time函数效果一样。
?>
