<?php
$str = "<a href='http://www.php.net'>PHP language website</a>";

$str_entity = htmlspecialchars($str);
$str_html = html_entity_decode($str_entity);

echo "���ú���htmlsepcialchars��";
echo "<br/>";
echo $str_entity;

echo "<br/>";
echo "<br/>";

echo "���ú���html_entity_decode��";
echo "<br/>";
echo $str_html;
?>
