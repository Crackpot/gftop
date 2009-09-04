<h3>条件语句</h3>
<?php
    if (!$_POST["guess"]){
?>
    <form name="form1" method="POST" action="3-10-2.php">
        请输入您猜想的数字：
        <input name="guess" type="text">
        <br/>(试试453)</br>
        选择您感兴趣的分类：
        <select name="category" >
            <option value="default" selected>请选择</option>
            <option value="news">新闻</option>
            <option value="weather">天气</option>
            <option value="sports">运动</option>
        </select><br/>
        <input type="submit" value="提交">
    </form>
<?php
    }
?>

<h5>1.if</h5>
<?php
    $secrectNumber = 453;
    if ($_POST["guess"] == $secrectNumber){
        echo "<p>Congratulations!</p>";
    }
?>

<h5>2.else</h5>
<?php
    $secrectNumber = 453;
    if ($_POST["guess"] == $secrectNumber){
        echo "<p>Congratulations!</p>";
    }
    else{
        echo "<p>Sorry!</p>";
    }
?>

<h5>3.elseif</h5>
<?php
    $secrectNumber = 453;
    $_POST["guess"] = 456;
    if ($_POST["guess"] == $secrectNumber){
        echo "<p>Congratulations!</p>";
    }
    elseif(abs ($_POST["guess"] - $secrectNumber) < 10){
        echo "<p>You're getting close!</p>";
    }
    else{
        echo "<p>Sorry!</p>";
    }
?>

<h5>4.switch</h5>
<?php
    $category = $_POST["category"];
    switch($category){
    case "news":
        print "<p>What's happening around the world?</p>";
        break;
    case "weather":
        print "<p>Your weekly forecast</p>";
        break;
    case "sports":
        print "<p>Latest sports highlights</p>";
        break;
    default:
        print "<p>Welcome to my web site!</p>";
    }
?>

<br/>
<a href=".">返回</a>
