<h1>文件包含语句</h1>

<h2>1.include</h2>
<a href="./include.php">include.php</a><br/>
<?php
    echo "include()不会验证是否已经包含了该文件。若包含，还会再次执行include()"."<br/>";
    include ("./include.php");
    include ("./include.php");
    /* the script continues here */
?>

<h2>2.include_once</h2>
<a href="./include_once.php">include_once.php</a><br/>
<?php
    echo "include_once()会首先验证是否已经包含了该文件。若包含，则不再执行include_once()"."<br/>";
    include_once ("./include_once.php");
    include_once ("./include_once.php");
    /* the script continues here */
?>

<h2>3.require</h2>
<a href="./require.php">require.php</a><br/>
<?php
    echo "require()不会验证是否已经包含了该文件。若包含，还会再次执行require()"."<br/>";
    require("./require.php");
    require("./require.php");
?>

<h2>4.require_once</h2>
<a href="./require_once.php">require_once.php</a><br/>
<?php
    echo "require_once()会首先验证是否已经包含了该文件。若包含，则不再执行require_once()"."<br/>";
    require_once ("./require_once.php");
    require_once ("./require_once.php");
?>
