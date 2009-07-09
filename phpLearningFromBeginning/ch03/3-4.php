<?php
session_start();

$_SESSION['user'] = 'KingKong';
$_SESSION['explain']='这是3-4.php的session变量';
echo '这个页面已经通过session保存了一些变量';
echo '<br/><a href="3-5.php">进入3-5.php</a>查看这些变量值';
?>