<?php
class Animal    //定义动物类
{
    public $blood;    //动物的热血和冷血属性 
    public $name;
    public function __construct($blood,$name=NULL)
    {
        $this->blood = $blood;
        if($name)
        {
            $this->name = $name;
        }
    }
}

class Mammal extends Animal    //哺乳动物，由Amimal类派生
{
    public $fur_color;     //皮毛颜色
    public $legs;
    function __construct($fur_color,$legs,$name=NULL)
    {
        parent::__construct("warm", $name);
        $this->fur_color = $fur_color;
        $this->legs = $legs;
    }
}

class Cat extends Mammal    //Dog类，由Mannal派生
{
    function __construct($fur_color,$name)
    {
        parent::__construct($fur_color,4,$name);
        self::bark();
    }

    function bark()
    {
        print("$this->name says, ' mew～ mew～ '");
    }
}

$cat_xiaobai = new Cat("white", "XiaoBai");
?>