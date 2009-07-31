<?php
$pop = "";
if(!empty($_POST['bname']) && !empty($_POST['bdesc']))    //添加一个新论坛
{
    $bname = $_POST['bname'];
    $bdesc = $_POST['bdesc'];
    
    mysql_connect("localhost","root","admin");
    mysql_select_db("mybbs") or die("Can't select database");
    $sql = "insert into boards (board_name,board_desc,build_time) values('".$bname."','".$bdesc."',NOW())";
    mysql_query($sql) or die ('ERROR: '.mysql_error());
    $pop = "添加成功";
}
?>
<html>
<head><title>论坛管理</title>
<link href="style.css" rel="stylesheet" type="text/css">
</head>
<body>

<div>====添加新论坛====</div>
<form name="addnew" action="" method="POST">
<div id="item">
    <div id="title">论坛名称：</div>
    <div id="input"><input type="text" name="bname" size="20" /></div>
</div>
<div id="item">
    <div id="title">论坛描述：</div>
    <div id="input"><input type="text" name="bdesc" size="30" /></div>
</div>
<div><input type="submit" name="smt" value="添加" /></div>
</form>
<div><?=$pop;?></div>

</body>
</html>