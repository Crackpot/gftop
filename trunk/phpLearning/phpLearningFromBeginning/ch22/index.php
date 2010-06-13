<?php
include_once("include/db_mysql.php");
include_once("include/common.php");
$conn = db_connect($h,$p,$u,$db);

if($conn)
{
    $sql = "select id,board_name,board_desc from boards order by id asc";
    $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
    
    if($num = mysql_num_rows($result))
    {
        $board_list = "";
        while($row = mysql_fetch_array($result))
        {
            $bid = $row['id'];
            $board_list .= "<div id=\"b_name\"> > <a href=\"list.php?bid=$bid\">".$row['board_name']."</a></div>";
            $board_list .= "<div id=\"b_desc\">".$row['board_desc']."</div><br/>";
        }
    }
    else
    {
        $board_list = "<div id=\"b_name\">".$ERR['NO_BOARD']."</div>";
    }
    close_db($conn);
}
$html_title = $HTML_TITLE['board'];

include_once("template/board.htm");
?>