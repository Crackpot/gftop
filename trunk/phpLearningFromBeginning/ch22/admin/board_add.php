<?php
$pop = "";
if(!empty($_POST['bname']) && !empty($_POST['bdesc']))    //���һ������̳
{
    $bname = $_POST['bname'];
    $bdesc = $_POST['bdesc'];
    
    mysql_connect("localhost","root","admin");
    mysql_select_db("mybbs") or die("Can't select database");
    $sql = "insert into boards (board_name,board_desc,build_time) values('".$bname."','".$bdesc."',NOW())";
    mysql_query($sql) or die ('ERROR: '.mysql_error());
    $pop = "��ӳɹ�";
}
?>
<html>
<head><title>��̳����</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>

<div>====�������̳====</div>
<form name="addnew" action="" method="POST">
<div id="item">
    <div id="title">��̳���ƣ�</div>
    <div id="input"><input type="text" name="bname" size="20" /></div>
</div>
<div id="item">
    <div id="title">��̳������</div>
    <div id="input"><input type="text" name="bdesc" size="30" /></div>
</div>
<div><input type="submit" name="smt" value="���" /></div>
</form>
<div><?=$pop;?></div>

</body>
</html>