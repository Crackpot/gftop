<?php
$xml_str = "<?xml version='1.0' encoding='UTF-8'?>";
$xml_str .= "<EMAILDOCUMENT>";
$xml_str .= "<TITLE>最近在学什么</TITLE>";
$xml_str .= "<FROM>小强</FROM>";
$xml_str .= "<TO>大强</TO>";
$xml_str .= "<BODY>";
$xml_str .= "我最近在学PHP，你呢？";
$xml_str .= "</BODY>";
$xml_str .= "</EMAILDOCUMENT>";

$xml = simplexml_load_string($xml_str);
var_dump($xml);
?>