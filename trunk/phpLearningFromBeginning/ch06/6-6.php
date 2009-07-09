<?php
echo "文件的所有者（用户ID）：";
echo fileowner("data.txt");
echo "<br>";
echo "<br>";

echo "文件的大小：";
echo filesize("data.txt");
echo "<br>";
echo "<br>";


echo "文件的类型：";
echo filetype("data.txt");
echo "<br>";
?>