<?php
$xml = simplexml_load_file("17-01.xml");

echo "==== " . $xml->getName() . "====<br/>";

foreach($xml->children() as $child)
{
    echo "--- ".$child->getName() . " --- <br/>";
    foreach($child->children() as $ch)
    {
        echo $ch->getName() . ": " . $ch . "<br/>";
    }
    echo "<br/>";
}
?>
