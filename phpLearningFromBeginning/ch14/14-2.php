<?php
class Cat
{
    private $name;
    function __construct()
    {
        echo "<b>构造函数被调用....</b><br/><br/>";
    }
    function __destruct()
    {
        echo "<b>析构函数被调用....</b><br/><br/>";
    }
    function set_name($name)
    {
        $this->name = $name;
    }
    function get_name()
    {
        echo "这只猫的名字叫：".$this->name."<br/><br/>";
    }
}

$mypet = new Cat;
echo "__construct()调用之后<br/><br/>";
$mypet->set_name("小白");
$mypet->get_name();
echo"类方法get_name()调用之后<br/><br/>";
?>
