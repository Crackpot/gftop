<?php
include_once("include/db_mysql.php");
include_once("include/common.php");
session_start();
$conn = db_connect($h,$p,$u,$db);

if(isset($_SESSION['user_id']) && $_SESSION['user_name'])
{
    $str_login = (empty($_SESSION['user_id'])) ? $FUNC['login2'] : "欢迎你，".$_SESSION['user_name']."！ <a href=\"logout.php\">注销退出</a>";
    $str_notlogin = (empty($_SESSION['user_id'])) ? $FUNC['notlogin'] : "";
}
else
{
    $str_login = $FUNC['login2'];
    $str_notlogin = $FUNC['notlogin'];
}
$error = "";

if(isset($_SESSION['user_id']))
    $user_id = $_SESSION['user_id'];
else
    $user_id = '';

if(isset($_GET['bid']))
    $bid = $_GET['bid'];
else
{
    $error = $ERR['NO_PARAM'];
    showerrpage($error);
    exit;
}
if(isset($_GET['page']))
    $page = $_GET['page'];

if(empty($bid) || !is_numeric($bid))
{
    $error = $ERR['NO_PARAM'];
    showerrpage($error);
    exit;
}
if(empty($page) || $page < 1 || !is_numeric($page))
    $page = 1;

$sql = "select board_name from boards where id=$bid";
$result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
if($num = mysql_num_rows($result))
{
    $row = mysql_fetch_array($result);
    $board_name = $row['board_name'];

    $sql = "select * from topics where bid=$bid and fid=0";
    $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
    $record_num = mysql_num_rows($result);
    if($record_num>0)
    {
        $page_size = 50;
        
        if($record_num%$page_size == 0)
            $page_count = $record_num/$page_size;
        else
            $page_count = intval($record_num/$page_size+1);
        
        if($page == 1)
        {
            $start = 0;
        }
        else
        {
            $start = ($page-1)*$page_size;
            $next = $page+1;//下页页码
            $prev = $page-1;//上页页码
        }
        $limit = " limit ".$start.",".$page_size;
        
        $sql = "select t.id,t.fid,u.user_id as user_id,u.user_name,content,DATE_FORMAT(post_time,'%Y-%m-%d %H:%i') ";
        $sql .= "as post_time,DATE_FORMAT(edit_time,'%Y-%m-%d %H:%i') as edit_time from topics t,users u ";
        $sql .= "where bid=".$bid." and fid=0 and t.user_id=u.user_id order by id desc".$limit;
        $result = mysql_query($sql) or die("ERROR: ".mysql_error()." <br/>SQL=".$sql);
        if($num = mysql_num_rows($result))
        {
            $topic_list = "<div><ul>";
            while($row = mysql_fetch_array($result))
            {
                $tid = $row['id'];
                $topic_list .= "<hr noshade size=\"1\" color=\"silver\" align=\"center\" width=\"100%\">";
                $topic_list .= "<li><a href=\"userinfo.php?uid=".$row['user_id']."\">".$row['user_name']."</a>";
                $topic_list .= "&nbsp;&nbsp;&nbsp;<font class=\"post_time\">".$row['post_time']."</font>";
                $str_mod = ($user_id == $row['user_id']) ? "<a href=\"mod_topic.php?bid=$bid&tid=$tid\">".$FUNC['modify']."</a>&nbsp;&nbsp;<a href=\"del_topic.php?bid=$bid&tid=$tid\">".$FUNC['delete']."</a>" : '';
                $topic_list .= "<span style='position:absolute;left:50%;'><a href='view.php?bid=$bid&tid=$tid'>".$FUNC['reply']."</a> ".$str_mod."</span>";
                $str_mdtime = ($row['edit_time'] != '0000-00-00 00:00') ? "(".$row['edit_time']."编辑过)" : '';
                $topic_list .= "<br/>&nbsp;&nbsp;&nbsp;&nbsp;".$row['content']." &nbsp;&nbsp;$str_mdtime</li>";
                $topic_list .= getReplyPost($tid);
            }
            $topic_list .= "</ul></div>";
            
            if($record_num > $page_size)
            {
                if($page == 1)
                {
                    $next = $page + 1;
                    $turn_page = "首页&nbsp;&nbsp;|&nbsp;&nbsp;上页&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"?bid=$bid&page=$next\">下页</a>";
                    $turn_page .= "&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"?bid=$bid&page=$page_count\">末页</a>";
                }
                elseif($page != $page_count)
                {
                    $turn_page = "<a href=\"?bid=$bid&page=1\">首页</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"?bid=$bid&page=$prev\">上页</a>";
                    $turn_page .= "&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"?bid=$bid&page=$next\">下页</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"?bid=$bid&page=$page_count\">末页</a>";
                }
                else
                {
                    $turn_page = "<a href=\"?bid=$bid&page=1\">首页</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"?bid=$bid&page=$prev\">上页</a>";
                    $turn_page .= "&nbsp;&nbsp;|&nbsp;&nbsp;下页&nbsp;&nbsp;|&nbsp;&nbsp;末页";
                }
            }
            else
            {
                $turn_page = "首页&nbsp;&nbsp;|&nbsp;&nbsp;上页&nbsp;&nbsp;|&nbsp;&nbsp;下页&nbsp;&nbsp;|&nbsp;&nbsp;末页";
            }
            $turn_page_tmp1 = "&nbsp;&nbsp;| <script language='javascript'>function pagejump()";
            $turn_page_tmp1 .= "{if (document.all.pagejmp.value == ''|| document.all.pagejmp.value < 0 ) ";
            $turn_page_tmp1 .= "{document.all.pagejmp.focus();alert('请输入有效跳转页码！');return false;}";
            $turn_page_tmp1 .= "else{this.location.href = '?bid=$bid'+'&page='+document.all.pagejmp1.value; target = '_self';}}</script> ";
            $turn_page_tmp1 .= "&nbsp;&nbsp;&nbsp;转到第 <input name=pagejmp size=3 onkeydown='if(window.event.keyCode==13) pagejump();'> 页 <a href=\"#\" onclick='pagejump();'>GO</a>";
            
            $turn_page_tmp2 = "&nbsp;&nbsp;| <script language='javascript'>function pagejump1()";
            $turn_page_tmp2 .= "{if (document.all.pagejmp1.value == ''|| document.all.pagejmp1.value < 0 ) ";
            $turn_page_tmp2 .= "{document.all.pagejmp1.focus();alert('请输入有效跳转页码！');return false;}";
            $turn_page_tmp2 .= "else{this.location.href = '?bid=$bid'+'&page='+document.all.pagejmp1.value; target = '_self';}}</script> ";
            $turn_page_tmp2 .= "&nbsp;&nbsp;&nbsp;转到第 <input name=pagejmp1 size=3 onkeydown='if(window.event.keyCode==13) pagejump1();'> 页 <a href=\"#\" onclick='pagejump1();'>GO</a>";
            
            $turn_page .= "&nbsp;&nbsp;|&nbsp;&nbsp;页次：".$page."/".$page_count."页";
            
            $turn_page1 = $turn_page.$turn_page_tmp1;
            $turn_page2 = $turn_page.$turn_page_tmp2;
            $turn_page1 .= "&nbsp;&nbsp;|&nbsp;&nbsp;".$FUNC['newpost']."&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"javascript:location.reload();\">".$FUNC['refresh']."</a>&nbsp;|&nbsp;";
            $turn_page2 .= "&nbsp;&nbsp;|&nbsp;&nbsp;".$FUNC['newpost']."&nbsp;&nbsp;|&nbsp;&nbsp;<a href=\"javascript:location.reload();\">".$FUNC['refresh']."</a>&nbsp;|&nbsp;";
        }
        else
        {
            $topic_list = ($page > $page_count) ? $ERR['INVALID_PAGE'] : $ERR['NO_TOPIC'];
            $turn_page1 = '';
            $turn_page2 = '';
        }
    }
    else
    {
        $topic_list = $ERR['NO_TOPIC'];
        $turn_page1 = '';
        $turn_page2 = '';
    }
}
else
{
    $error = $ERR['BOARD_NOT_EXIST'];
    showerrpage($error);
    exit;
}

$html_title = $HTML_TITLE['list'];
$board_name_list = getBoardList();
$user_rank_list = userRank($bid);

close_db($conn);

include_once("template/list.htm");
?>