<?php
class Test
{
    public function __get($prop_name)
    {
        echo "获取属性：（ $prop_namen ）<br/>";
    }
    public function __set($prop_name, $value)
    {
        echo "设置属性 $prop_name 的值为 '$value'";
    }

}
$test = new Test();
$test->Name;
$test->Name = "测试设置";
?>