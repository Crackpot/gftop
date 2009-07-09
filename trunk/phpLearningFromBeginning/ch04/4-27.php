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
        echo $c.'是数组olympic的索引';
        echo '<br/>';
        echo '<br/>';
    }
    else
    {
        echo $c.'不是数组olympic的索引';
        echo '<br/>';
        echo '<br/>';
    }
}
?>