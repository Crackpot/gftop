<?php
class Test
{
    public function __get($prop_name)
    {
        echo "��ȡ���ԣ��� $prop_namen ��<br/>";
    }
    public function __set($prop_name, $value)
    {
        echo "�������� $prop_name ��ֵΪ '$value'";
    }

}
$test = new Test();
$test->Name;
$test->Name = "��������";
?>