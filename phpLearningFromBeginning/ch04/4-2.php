<?php
$ms_office = array(
'word',
'excel',
'outlook',
'access'
);

for($i=0; $i<4; $i++)
{
    echo "����� ".($i+1)." ��Ԫ���ǣ�";
    echo $ms_office[$i];
    echo "<br/>";
    echo "<br/>";
}
?>