<?php
$html = "<b>粗体字符</b><a href=howdy.html>可点击的连接</a>";

preg_match_all ("/(<([\w]+)[^>]*>)(.*)(<\/\\2>)/", $html, $matches);

for ($i=0; $i< count($matches[0]); $i++)
{
    echo "匹配：".$matches[0][$i]."\n";;
    echo "第一部分：".$matches[1][$i]."\n";
    echo "第二部分：".$matches[3][$i]."\n";
    echo "第三部分：".$matches[4][$i]."\n\n";
}
?>