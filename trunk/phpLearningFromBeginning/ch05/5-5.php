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
echo "Ìæ»»Ç°£º".$str;

echo "<br/>";
echo "<br/>";
echo "Ìæ»»ºó£º".$new_str;
?>