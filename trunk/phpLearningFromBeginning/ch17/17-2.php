<?php
$parser=xml_parser_create();                        //初始化XML分析器

function start($parser,$elem_name,$elem_attrs)      //在一个元素开始时调用的函数
{
    switch($elem_name)
    {
        case "BOOKS":
            echo "<b>-- 图书信息 --</b><br/><br/>";
            break;
        case "TITLE":
            echo "<b>书名: </b>";
            break;
        case "AUTHOR":
            echo "<b>作者: </b>";
            break;
        case "PUBLISHER":
            echo "<b>出版社: </b>";
            break;
        case "PRICE":
            echo "<b>价格: </b>";
            break;
    }
}

function stop($parser,$elem_name)                   //在一个元素结束时调用的函数
{
    echo "<br />";
}

function char($parser,$data)                        //当找到一个字符数据时调用该函数
{
    echo $data;
}


xml_set_element_handler($parser,"start","stop");    //指定元素处理器
xml_set_character_data_handler($parser,"char");     //指定字符数据处理器

$fp=fopen("17-1.xml","r");                          //打开XML文件
while($data=fread($fp,1024))                        //循环读入XML文件中的内容
{
    xml_parse($parser,$data,feof($fp)) or 
    die(sprintf("XML错误: %s at line %d", 
    xml_error_string(xml_get_error_code($parser)),
    xml_get_current_line_number($parser)));
}

xml_parser_free($parser);                           //释放XML分析器资源
?>