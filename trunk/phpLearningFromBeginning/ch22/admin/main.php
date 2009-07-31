<?php
session_start();
if(empty($_SESSION['ad']))
{
    echo '<p><font color="red">请登录后执行此操作</font></p>';
    exit;
}
?>
<html>
<title> 后台管理界面 </title>
</head>
<frameset cols="100,*">

<frame src="framelist.htm">
<frame src="topic_list.php" name="showframe">

</frameset>
</html>