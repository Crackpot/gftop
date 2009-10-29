<?php
class Counter
{
    private static $count = 0;
    function __construct()
    {
        echo '<b>计数开始!</b><br/><br/>';
    }
    function __destruct()
    {
        echo '<b>计数结束!</b><br/><br/>';
    }
    static function get_count()
    {
        return self::$count;
    }
    
    static function counts()
    {
    	self::$count++;
    }
}

$c = new Counter();
$i = 0;
while($i<5)
{
	Counter::counts();
    $i = Counter::get_count();
    echo Counter::get_count() . "<br/><br/>";
}
?>