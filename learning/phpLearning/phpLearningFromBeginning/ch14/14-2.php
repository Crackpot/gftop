<?php
class Cat
{
    private $name;
    function __construct()
    {
        echo "<b>���캯��������....</b><br/><br/>";
    }
    function __destruct()
    {
        echo "<b>��������������....</b><br/><br/>";
    }
    function set_name($name)
    {
        $this->name = $name;
    }
    function get_name()
    {
        echo "��ֻè�����ֽУ�".$this->name."<br/><br/>";
    }
}

$mypet = new Cat;
echo "__construct()����֮��<br/><br/>";
$mypet->set_name("С��");
$mypet->get_name();
echo"�෽��get_name()����֮��<br/><br/>";
?>
