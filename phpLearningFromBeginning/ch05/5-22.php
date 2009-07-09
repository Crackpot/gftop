<?php
$str1 = 'This is a secret';
$str2 = 'root';

echo '原字符串：';
echo '<br/>';
echo 'str1='.$str1;
echo 'str2='.$str2;
echo '<br/>';
echo '<br/>';

echo '使用md5加密：';
echo '<br/>';
echo "md5($str1)=".md5($str1);
echo '<br/>';
echo "md5($str2)=".md5($str2);

echo '<br/>';
echo '<br/>';

echo '使用sha1加密：';
echo '<br/>';
echo "sha1($str1)=".sha1($str1);
echo '<br/>';
echo "sha1($str2)=".sha1($str2);
?>