<?php
$last_access = fileatime("data.txt");
echo "文件最后的访问时间是：";
echo date("l F d, Y", $last_access);
echo "<br>";
echo "<br>";

$last_modify = filemtime("data.txt");
echo "文件最后的修改时间：";
echo date("l F d, Y", $last_modify);
echo "<br>";
echo "<br>";

$last_modify_inode = filectime("data.txt");
echo "文件最后的改变时间：";
echo date("l F d, Y", $last_modify_inode);
echo "<br>";
echo "<br>";
?>