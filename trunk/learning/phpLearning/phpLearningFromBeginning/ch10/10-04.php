<?php
$file = getenv('SCRIPT_FILENAME');
echo "<b>当前运行的程序：</b>";
echo $file;
echo "<hr>";
echo "<br/>";

echo "该程序所有者：".get_current_user();
echo "<br/>";
echo "<br/>";
echo "该进程ID号：".getmypid();
?>
