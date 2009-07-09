<?php
echo "PHP当前的工作目录：";

echo "<br/>";
echo getcwd();
echo "<br/>";

chdir("dir_test");  //改变工作目录至当前目录的dir_test目录下

echo "<br/>";
echo "改变工作目录后，工作目录变为：";
echo "<br/>";

echo getcwd();
?>