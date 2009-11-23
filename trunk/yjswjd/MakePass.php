<?php

function MakePass($length)

{

$possible = "0123456789!@#$%^&*()_+".

             "abcdefghijklmnopqrstuvwxyz".

             "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

$str = "";

while(strlen($str) < $length)

{

  $str .= substr($possible, (rand() % strlen($possible)), 1);

}
echo $str ;
return($str);

}

?> 
<?php
MakePass(10);
?>