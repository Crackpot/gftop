<?php
$html = "<b>�����ַ�</b><a href=howdy.html>�ɵ��������</a>";

preg_match_all ("/(<([\w]+)[^>]*>)(.*)(<\/\\2>)/", $html, $matches);

for ($i=0; $i< count($matches[0]); $i++)
{
    echo "ƥ�䣺".$matches[0][$i]."\n";;
    echo "��һ���֣�".$matches[1][$i]."\n";
    echo "�ڶ����֣�".$matches[3][$i]."\n";
    echo "�������֣�".$matches[4][$i]."\n\n";
}
?>