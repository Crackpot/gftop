<?php
$root = getenv('DOCUMENT_ROOT');
$port = getenv('SERVER_PORT');
$file = getenv('SCRIPT_NAME');
$ua = getenv('HTTP_USER_AGENT');
$method = getenv('REQUEST_METHOD');
$protocol = getenv('SERVER_PROTOCOL');

echo "<b>通过函数getenv()获取环境变量</b><hr>";
echo "<b>服务器文档根目录：</b>".$root;
echo "<br/>";
echo "<br/>";

echo "<b>服务器端口：</b>".$port;
echo "<br/>";
echo "<br/>";

echo "<b>当前执行文件：</b>".$file;
echo "<br/>";
echo "<br/>";

echo "<b>用户UA：</b>".$ua;
echo "<br/>";
echo "<br/>";

echo "<b>请求方法：</b>".$method;
echo "<br/>";
echo "<br/>";

echo "<b>传输协议：</b>".$protocol;
?>