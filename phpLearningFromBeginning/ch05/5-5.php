<?php
$str = "I prefer to use JSP,PHP,ASP!";

$page_lan = array(
"JSP",
"PHP",
"ASP"
);

$base_lan = array(
"C",
"C++",
"Java"
);

$new_str = str_replace($page_lan,$base_lan,$str);
echo "�滻ǰ��".$str;

echo "<br/>";
echo "<br/>";
echo "�滻��".$new_str;
?>