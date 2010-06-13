<?php
class Student
{
    private $id, $name;
    public function __construct($s_id, $s_name)
    {
        $this->id = $s_id;
        $this->name = $s_name;
    }
    public function __toString()
	{
	    return "$this->id : $this->name";
	}
}
$stu = new Student(1, 'George Wesley');
echo '<b>以下输出对象时，实际调用了方法__toString()</b><br/><br/>';
echo $stu
?>