<?php
class Person
{
    private $name;
    public function set_name($name)
    {
        $this->name = $name;
    }
    public function get_name()
    {
        echo "My name is ".$this->name."<br/>";
    }
}

$boy = new Person;
$boy->set_name("Harry Pottor");
$boy->get_name();

$girl = new Person;
$girl->set_name("Emma");
$girl->get_name();
?>
