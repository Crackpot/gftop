<?php
session_start();
if(empty($_SESSION['ad']))
{
    echo '<p><font color="red">���¼��ִ�д˲���</font></p>';
    exit;
}
?>
<html>
<title> ��̨������� </title>
</head>
<frameset cols="100,*">

<frame src="framelist.htm">
<frame src="topic_list.php" name="showframe">

</frameset>
</html>