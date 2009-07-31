<?php
$parser=xml_parser_create();                        //��ʼ��XML������

function start($parser,$elem_name,$elem_attrs)      //��һ��Ԫ�ؿ�ʼʱ���õĺ���
{
    switch($elem_name)
    {
        case "BOOKS":
            echo "<b>-- ͼ����Ϣ --</b><br/><br/>";
            break;
        case "TITLE":
            echo "<b>����: </b>";
            break;
        case "AUTHOR":
            echo "<b>����: </b>";
            break;
        case "PUBLISHER":
            echo "<b>������: </b>";
            break;
        case "PRICE":
            echo "<b>�۸�: </b>";
            break;
    }
}

function stop($parser,$elem_name)                   //��һ��Ԫ�ؽ���ʱ���õĺ���
{
    echo "<br />";
}

function char($parser,$data)                        //���ҵ�һ���ַ�����ʱ���øú���
{
    echo $data;
}


xml_set_element_handler($parser,"start","stop");    //ָ��Ԫ�ش�����
xml_set_character_data_handler($parser,"char");     //ָ���ַ����ݴ�����

$fp=fopen("17-1.xml","r");                          //��XML�ļ�
while($data=fread($fp,1024))                        //ѭ������XML�ļ��е�����
{
    xml_parse($parser,$data,feof($fp)) or 
    die(sprintf("XML����: %s at line %d", 
    xml_error_string(xml_get_error_code($parser)),
    xml_get_current_line_number($parser)));
}

xml_parser_free($parser);                           //�ͷ�XML��������Դ
?>