<?php
$input = "Story";

echo '/'.str_pad($input, 10).'/';
echo '<br/>';
echo '<br/>';

echo str_pad($input, 10, "-*", STR_PAD_LEFT);
echo '<br/>';
echo '<br/>';

echo str_pad($input, 10, "*", STR_PAD_BOTH);
echo '<br/>';
echo '<br/>';

echo str_pad($input, 6 , "***");
?>