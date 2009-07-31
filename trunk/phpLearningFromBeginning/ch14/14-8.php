<?php
class doClone
{
    private $id,$name,$address;
    
    public function __construct($id=0,$name='',$address='')
    {
        $this->id = $id;
        $this->name = $name;
        $this->address = $address;
    }
    public function get_id()
    {
        return $this->id;
    }
    public function get_name()
    {
        return $this->name;
    }
    public function get_address()
    {
        return $this->address;
    }
    public function __clone()
    {
        $this->id = $this->id+1;
        $this->name = 'Kong';
        $this->address = "America";
    }
}

$cle = new doClone(99,'King','Island');
echo '<b>clone֮ǰ������ $cle �����ԣ�</b>';
echo '<br/>';
echo 'id = '.$cle->get_id() . "<br/>";
echo 'name = '.$cle->get_name() . "<br/>";
echo 'address = '.$cle->get_address();
echo '<br/>';
echo '<br/>';

$cle_cloned = clone $cle;
echo '<b>clone֮�󣬶��� $cle �����ԣ�</b>';
echo '<br/>';
echo 'id = '.$cle->get_id() . "<br/>";
echo 'name = '.$cle->get_name() . "<br/>";
echo 'address = '.$cle->get_address();
echo '<br/>';
echo '<br/>';

echo '<b>clone֮�󣬶��� $cle_cloned �����ԣ�</b>';
echo '<br/>';
echo 'id = '.$cle_cloned->get_id() . "<br/>";
echo 'name = '.$cle_cloned->get_name() . "<br/>";
echo 'address = '.$cle_cloned->get_address();
?>