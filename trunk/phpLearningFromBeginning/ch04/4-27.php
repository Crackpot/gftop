<?php
$olympic = array(
'Barcelona'=>1992,
'Atlanta'=>1996,
'Sydney'=>2000,
'Athens'=>2004,
'Beijing'=>2008
);

$city = array(
'Rome',
'Athens',
'Shanghai'
);

foreach($city as $c)
{
    if(array_key_exists($c, $olympic))
    {
        echo $c.'������olympic������';
        echo '<br/>';
        echo '<br/>';
    }
    else
    {
        echo $c.'��������olympic������';
        echo '<br/>';
        echo '<br/>';
    }
}
?>