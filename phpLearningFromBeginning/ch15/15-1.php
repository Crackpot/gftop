<?php
$arr_date = array(
'2004-06-01',
'2005-0x-10',
'12-12-12',
'2000-12-25 00:10:20',
'2007-12-05'
);

for ($i=0; $i<5; ++$i)
{
	$date = $arr_date[$i];
	if(ereg("([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})", $date, $regs))
	{
	    echo "�����ַ���$date ����'YYYY-MM-DD'��ʽ��";
	    echo "$regs[1].$regs[2].$regs[3]<br/><br/>";
	}
	else
	{
	    echo "<b>�����ַ���$date ������'YYYY-MM-DD'��ʽ�������ַ���</b><br/><br/>";
	}
}
?>