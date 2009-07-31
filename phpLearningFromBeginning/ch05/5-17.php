<?php
$str = "<a href='http://www.php.net'>PHP language website</a>";

$str_entity = htmlspecialchars($str);
$str_html = html_entity_decode($str_entity);

echo "调用函数htmlsepcialchars后：";
echo "<br/>";
echo $str_entity;

echo "<br/>";
echo "<br/>";

echo "调用函数html_entity_decode后：";
echo "<br/>";
echo $str_html;
?>
