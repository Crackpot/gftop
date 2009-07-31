<?php
class Animal    //���嶯����
{
    public $blood;    //�������Ѫ����Ѫ���� 
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

class Mammal extends Animal    //���鶯���Amimal������
{
    public $fur_color;     //Ƥë��ɫ
    public $legs;
    function __construct($fur_color,$legs,$name=NULL)
    {
        parent::__construct("warm", $name);
        $this->fur_color = $fur_color;
        $this->legs = $legs;
    }
}

class Cat extends Mammal    //Dog�࣬��Mannal����
{
    function __construct($fur_color,$name)
    {
        parent::__construct($fur_color,4,$name);
        self::bark();
    }

    function bark()
    {
        print("$this->name says, ' mew�� mew�� '");
    }
}

$cat_xiaobai = new Cat("white", "XiaoBai");
?>