<?php
echo "<b>��ǰ���б������ģ���������</b>";
echo "<hr>";

$exten_list = get_loaded_extensions();

foreach($exten_list as $extension)
{
    echo "$extension <br/>";
    echo "<ul>";
    $ext_func = get_extension_funcs($extension);
    foreach($ext_func as $func)
    {
        echo "<li> $func </li>";
    }
    echo "</ul>";
}
?>