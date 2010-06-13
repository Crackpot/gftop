<?php
$xml_str = "<?xml version='1.0'?>";
$xml_str .= "<books>";
$xml_str .= "<book>";
$xml_str .= "<title>Harry Potter</title>";
$xml_str .= "<author>J.K.Rowling</author>";
$xml_str .= "<publisher>Warner Bros.</publisher>";
$xml_str .= "<price>39.0</price>";
$xml_str .= "</book>";
$xml_str .= "</books>";

$dom = new DOMDocument;
$dom->loadXML($xml_str);

echo $dom->saveXML();
$dom->save("test.xml");
?>