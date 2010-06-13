<?php
/**
 * 论坛功能函数
 */
function getReplyPost($tid)
{
    global $FUNC,$bid;
    $reply_list = "";
    $sql = "select t.id,t.fid,u.user_id as user_id,u.user_name,content,DATE_FORMAT(post_time,'%Y-%m-%d %H:%i') as post_time from topics t,users u where fid=".$tid." and t.user_id=u.user_id order by id asc";
    $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
    if($num = mysql_num_rows($result))
    {
        while($row = mysql_fetch_array($result))
        {
            $reply_list .= "<ul>";
            $reply_list .= "<li><a href=\"userinfo.php?uid=".$row['user_id']."\">".$row['user_name']."</a>";
            $reply_list .= "&nbsp;&nbsp;&nbsp;<font class=\"post_time\">".$row['post_time']."</font>";
            $str_mod = (($_SESSION['user_id']) == $row['user_id']) ? "<a href=\"mod_topic.php?bid=$bid&tid=$tid\">".$FUNC['modify']."</a> <a href=\"del_topic.php?bid=$bid&tid=$tid\">".$FUNC['delete']."</a>" : '';
            $reply_list .= "<br/>&nbsp;&nbsp;&nbsp;&nbsp;".$row['content']." $str_mod"."</li>";
            $reply_list .= "</ul>";
        }
    }
    return $reply_list;
}

function getBoardList()
{
    $board_name_list = "";
    $sql = "select id,board_name,board_desc from boards";
    $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
    if($num = mysql_num_rows($result))
    {
        $board_name_list = "<div style=\"margin:3px;padding:3px;font-size:12px;text-align:left;\">论坛列表</div>";
        while($row = mysql_fetch_array($result))
        {
            $board_name_list .= "<div style=\"margin:5px;padding:3px;border-left:2px solid #434A56;background-color:#F2F3F4;\">";
            $board_name_list .= "<a href=\"list.php?bid=".$row['id']."\" title=\"".$row['board_desc']."\">";
            $board_name_list .= $row['board_name'];
            $board_name_list .= "</a></div>";
        }
        $board_name_list .= "<br/>";
    }
    return $board_name_list;
}

function userRank($bid)
{
    $user_rank_list = "";
    $sql = "select u.user_id as id,user_name,count(*) as post_count from topics t, users u where t.user_id=u.user_id and bid=$bid group by t.user_id,user_name order by post_count desc";
    $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
    if($num = mysql_num_rows($result))
    {
        $user_rank_list = "<div style=\"margin:3px;padding:3px;font-size:12px;text-align:left;\">本版发贴排行榜</div>";
        while($row = mysql_fetch_array($result))
        {
            $user_rank_list .= "<div style=\"margin:5px;padding:3px;border-left:2px solid #434A56;background-color:#F2F3F4;\">";
            $user_rank_list .= "<a href=\"userinfo.php?uid=".$row['id']."\">";
            $user_rank_list .= $row['user_name'];
            $user_rank_list .= "</a>";
            $user_rank_list .= " (".$row['post_count'].")</div>";
        }
        $user_rank_list .= "<br/>";
    }
    return $user_rank_list;
}
?>