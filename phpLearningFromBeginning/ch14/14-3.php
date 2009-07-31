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
        return $this->name;
    }
}

class Worker extends Person    //Worker类继承自Person，使用关键字extends
{
    private $salary;
    
    public function set_salary($salary)
    {
        $this->salary = $salary;
    }
    public function get_salary()
    {
        return $this->salary;
    }
}

$a_work = new Worker;
$a_work->set_name('Paul');
$a_work->set_salary(3500);

$name = $a_work->get_name();
$salary = $a_work->get_salary();
echo $name."的月薪为".$salary;
?>